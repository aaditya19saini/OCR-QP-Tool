"""Tables + figures for the report (deterministic from outputs/master.csv).

Usage: python -m pyq.report        -> outputs/tables/*.csv, outputs/figures/NN-*.png
Main scope = current-format papers (pyq.stats.scope); old-format papers get their own table.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from . import stats
from .common import OUTPUTS, load_yaml, setup_logging, verify_manifest

TABLES, FIGS = OUTPUTS / "tables", OUTPUTS / "figures"
PALETTE = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00", "#F0E442", "#000000"]  # Okabe-Ito


def syllabus_subtopics() -> pd.DataFrame:
    tax = load_yaml("taxonomy.yaml")["subjects"]
    return pd.DataFrame([(s, t, st) for s, ts in tax.items() for t, sts in ts.items() for st in sts],
                        columns=["subject", "topic", "subtopic"])


def build_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    cur = stats.scope(df)
    years = sorted(cur.year.unique())
    topic = stats.topic_table(cur, "topic").reset_index()
    sub = stats.topic_table(cur, "subtopic").reset_index()
    sub["tier"] = stats.tiers(sub).values
    # syllabus subtopics never tested in scope: listed with 0, tier "untested" (may be new to the 2026 syllabus)
    allsub = syllabus_subtopics().merge(sub, on=["subject", "topic", "subtopic"], how="left")
    allsub["questions"] = allsub["questions"].fillna(0).astype(int)
    allsub["tier"] = allsub["tier"].map(lambda v: "untested" if pd.isna(v) else str(int(v)))
    old = stats.topic_table(stats.scope(df, "old"), "topic").reset_index()
    out = {
        "topics_current": topic,
        "subtopics_current": allsub.sort_values(["questions", "mean_marks_share"], ascending=False),
        "year_topic_share": stats.year_topic(cur, years, "topic", "share"),
        "format_mix": stats.format_mix(df),
        "archetypes_current": stats.archetypes(cur).reset_index(),
        "repeats": df[df.repeat_kind.notna()].groupby(["era", "repeat_kind"]).size().rename("rows").reset_index(),
        "topics_old_2012_2014": old,
    }
    for k, v in out.items():
        assert not v.empty, k
    return out


def footer(fig, n_q, years):
    fig.text(0.01, 0.005, f"Source: JAM MS papers {years[0]}–{years[-1]} (current format); n = {n_q} questions, {len(years)} papers",
             fontsize=7, color="#555")


def figures(t: dict, n_q: int, years: list[int]) -> None:
    FIGS.mkdir(parents=True, exist_ok=True)
    tp = t["topics_current"].sort_values("mean_marks_share", ascending=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(tp.topic, tp.mean_marks_share * 100, color=PALETTE[0])
    ax2 = ax.twinx(); ax2.plot(tp.topic, tp.mean_marks_share.cumsum() * 100, color=PALETTE[5], marker="o")
    ax.set_ylabel("Mean share of paper marks (%)"); ax2.set_ylabel("Cumulative share (%)"); ax2.set_ylim(0, 105)
    ax.set_title(f"Marks weightage by syllabus topic, {years[0]}–{years[-1]} (Pareto)")
    ax.tick_params(axis="x", rotation=60, labelsize=8); plt.setp(ax.get_xticklabels(), ha="right")
    footer(fig, n_q, years); fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "01-pareto-marks-share.png", dpi=200); plt.close(fig)

    m = t["year_topic_share"][tp.topic] * 100
    fig, ax = plt.subplots(figsize=(10, 5.5))
    im = ax.imshow(m.T.values, aspect="auto", cmap="viridis")
    ax.set_xticks(range(len(m.index)), m.index); ax.set_yticks(range(len(m.columns)), m.columns, fontsize=8)
    for i, y in enumerate(m.index):
        for j, c in enumerate(m.columns):
            ax.text(i, j, f"{m.loc[y, c]:.0f}", ha="center", va="center", fontsize=6, color="w" if m.loc[y, c] < 10 else "k")
    fig.colorbar(im, label="Share of that paper's marks (%)"); ax.set_xlabel("Exam year")
    ax.set_title("Marks share by topic and year")
    footer(fig, n_q, years); fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "02-year-topic-heatmap.png", dpi=200); plt.close(fig)

    st = t["subtopics_current"]; st = st[st.questions > 0].nlargest(25, "appearance_rate").iloc[::-1]
    colors = st.tier.map({"1": PALETTE[0], "2": PALETTE[1], "3": PALETTE[3]})
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.barh(st.subtopic, st.appearance_rate * 100, color=colors)
    ax.set_xlabel(f"Papers containing the subtopic (% of {len(years)})"); ax.tick_params(axis="y", labelsize=7)
    ax.set_title("Most consistently tested subtopics (top 25; colour = tier: blue 1, orange 2)")
    footer(fig, n_q, years); fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "03-subtopic-appearance.png", dpi=200); plt.close(fig)

    fm = t["format_mix"]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    fm.plot.bar(stacked=True, ax=ax, color=PALETTE[: len(fm.columns)])
    ax.set_ylabel("Questions"); ax.set_xlabel("Exam year"); ax.legend(title="Format", fontsize=8)
    ax.set_title(f"Question format mix per paper, {fm.index.min()}–{fm.index.max()} (2012–2014 are old formats)")
    fig.text(0.01, 0.005, f"Source: JAM MS papers {fm.index.min()}–{fm.index.max()}; top-level questions", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "04-format-mix.png", dpi=200); plt.close(fig)

    ar = t["archetypes_current"].head(20).iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.barh(ar.archetype, ar.papers, color=PALETTE[2])
    ax.set_xlabel(f"Papers in which the problem structure appears (of {len(years)})"); ax.tick_params(axis="y", labelsize=7)
    ax.set_title("Most recurring problem structures (archetypes), top 20")
    footer(fig, n_q, years); fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "05-top-archetypes.png", dpi=200); plt.close(fig)


def pct(x: float) -> str:
    return f"{x * 100:.1f}%"


def html_table(df: pd.DataFrame) -> str:
    return df.to_html(index=False, border=0, classes="t", escape=True, na_rep="—")


def write_html(df: pd.DataFrame, t: dict) -> str:
    """Report prose. Every number is computed here from the tables; interpretation is labelled as such."""
    cur = stats.scope(df)
    years = sorted(cur.year.unique())
    n_q, n_p = len(cur), len(years)
    tp = t["topics_current"].sort_values("mean_marks_share", ascending=False)
    sub = t["subtopics_current"]
    yt = t["year_topic_share"]
    early, late = yt.loc[years[0]:years[0] + 3].mean(), yt.loc[years[-1] - 2:years[-1]].mean()
    shift = (late - early).sort_values()
    subj = cur.groupby("subject").marks.sum() / cur.marks.sum()
    top3 = tp.head(3)
    near = int((cur.repeat_kind == "near").sum())
    cog = cur.cognitive_type.value_counts(normalize=True)
    untested = sub[sub.tier == "untested"]
    # subtopics whose first appearance in scope is the latest paper (new-syllabus topics show up here)
    first_yr = cur.groupby("subtopic").year.min()
    fresh = cur[cur.subtopic.isin(first_yr[first_yr == years[-1]].index)]
    fresh_subs = sorted(fresh.subtopic.unique())
    fresh_marks = int(fresh.marks.sum())
    topic_first = cur.groupby("topic").year.min()
    old_tp = tp[~tp.topic.str.startswith("Differential Equations") & tp.topic.map(topic_first).lt(years[-1])]
    tier1 = sub[sub.tier == "1"].sort_values("mean_marks_share", ascending=False)
    ar = t["archetypes_current"].head(10)
    old = t["topics_old_2012_2014"].sort_values("mean_marks_share", ascending=False).head(6)
    ode_years = sorted(df[df.topic.str.startswith("Differential Equations")].year.unique())
    f = lambda x: f'<span class="n">{x}</span>'  # noqa: E731

    topic_tbl = tp[["subject", "topic", "questions", "papers_appeared", "mean_marks_share", "recent_questions", "n_archetypes"]].copy()
    topic_tbl["mean_marks_share"] = topic_tbl.mean_marks_share.map(pct)
    topic_tbl.columns = ["Subject", "Topic", "Questions", f"Papers (of {n_p})", "Mean marks share", f"Questions {years[-3]}–{years[-1]}", "Problem structures"]
    t1 = tier1[["topic", "subtopic", "questions", "papers_appeared", "mean_marks_share"]].copy()
    t1["papers_appeared"] = t1.papers_appeared.astype(int); t1["mean_marks_share"] = t1.mean_marks_share.map(pct)
    t1.columns = ["Topic", "Subtopic", "Questions", f"Papers (of {n_p})", "Mean marks share"]
    alloc = tp[["topic", "mean_marks_share"]].copy()
    alloc = alloc[~alloc.topic.str.startswith("Differential Equations")]
    alloc["Suggested study time"] = (alloc.mean_marks_share / alloc.mean_marks_share.sum() * 0.9).map(pct)
    alloc = alloc.drop(columns="mean_marks_share").rename(columns={"topic": "Topic"})
    ar_tbl = ar[["topic", "archetype", "papers", "questions", "examples"]].rename(columns=str.title)
    shift_rows = "".join(f"<li>{s}: {pct(early[s])} → {pct(late[s])}</li>" for s in list(shift.index[:3]) + list(shift.index[-3:]))

    return f"""<!doctype html><html><head><meta charset="utf-8"><title>JAM MS PYQ Report</title><style>
body{{font:11pt/1.5 system-ui,sans-serif;max-width:900px;margin:2em auto;padding:0 1em;color:#111}}
h1{{font-size:1.6em}} h2{{border-bottom:1px solid #ccc;margin-top:1.6em}} img{{max-width:100%}}
table.t{{border-collapse:collapse;font-size:9pt;margin:.6em 0}} .t td,.t th{{padding:3px 7px;border-bottom:1px solid #ddd;text-align:left}}
.ev{{font-size:.85em;padding:1px 6px;border-radius:3px;background:#eef}} .hyp{{background:#fff4e0;padding:.5em 1em;border-left:3px solid #E69F00}}
.n{{font-weight:600}} @media print{{h2{{break-before:auto}} img{{break-inside:avoid}}}}
</style></head><body>
<h1>IIT JAM Mathematical Statistics: Previous-Year Paper Analysis</h1>
<p>Scope: {n_p} current-format papers ({years[0]}–{years[-1]}, 60 questions / 100 marks each), {n_q} questions. Old-format papers 2012–2014 are reported separately. Taxonomy: official JAM 2026 MS syllabus (plus a pre-2026 Differential Equations topic). Evidence tags: <span class="ev">strong</span> = seen in nearly every paper; <span class="ev">moderate</span> = consistent but small or recent; <span class="ev">weak</span> = few observations.</p>

<h2>1. Summary</h2><ul>
<li><b>Statistics carries {f(pct(subj['Statistics']))} of marks, Mathematics {f(pct(subj['Mathematics']))}.</b> <span class="ev">strong</span></li>
<li><b>{top3.topic.iloc[0]}, {top3.topic.iloc[1]} and {top3.topic.iloc[2]}</b> are the heaviest topics ({pct(top3.mean_marks_share.iloc[0])}, {pct(top3.mean_marks_share.iloc[1])}, {pct(top3.mean_marks_share.iloc[2])} of a paper on average); together {f(pct(top3.mean_marks_share.sum()))}. <span class="ev">strong</span></li>
<li>Every main syllabus topic tested before {years[-1]} (so not the dropped Differential Equations or the topics new in {years[-1]}) appears in at least {int(old_tp.papers_appeared.min())} of {n_p} papers: <b>no topic is skippable</b>. <span class="ev">strong</span></li>
<li><b>The paper is shifting</b> from calculus towards distribution theory: comparing {years[0]}–{years[0]+3} with {years[-1]-2}–{years[-1]}, {shift.index[0]} fell {pct(early[shift.index[0]])} → {pct(late[shift.index[0]])} while {shift.index[-1]} rose {pct(early[shift.index[-1]])} → {pct(late[shift.index[-1]])}. <span class="ev">moderate</span></li>
<li><b>{f(pct(near / n_q))}</b> of questions ({near}/{n_q}) reuse the problem structure of an earlier question with new numbers or set-up; 0 are word-for-word repeats. Drilling past papers by structure pays off. <span class="ev">strong</span></li>
<li>Differential Equations appear only in {ode_years[0]}–{ode_years[-1]} and not since; they are not in the 2026 syllabus. <span class="ev">strong</span></li>
<li><b>New-syllabus topics arrived in {years[-1]}.</b> {len(fresh_subs)} subtopics never tested in {years[0]}–{years[-2]} appeared for the first time in the {years[-1]} paper: {f(len(fresh))} questions, {f(fresh_marks)} of 100 marks ({", ".join(fresh_subs)}). <span class="ev">strong</span> (one paper; their future weight is unknown)</li>
<li>{len(untested)} syllabus subtopics are still untested in {years[0]}–{years[-1]}{(" (" + ", ".join(untested.subtopic) + ")") if len(untested) else ""}. Treat them as unknown, not low priority.</li></ul>

<h2>2. Examination overview</h2>
<p>Format since {years[0]}: 30 MCQ (Section A), 10 MSQ (B), 20 NAT (C); 10+20 one/two-mark MCQs, two-mark MSQs, 10+10 one/two-mark NATs. Question styles: numerical {pct(cog.get('numerical', 0))}, application {pct(cog.get('application', 0))}, conceptual {pct(cog.get('conceptual', 0))}, everything else {pct(1 - cog.get('numerical', 0) - cog.get('application', 0) - cog.get('conceptual', 0))} (subjective labels).</p>
<img src="../figures/04-format-mix.png" alt="Question format mix per year">

<h2>3. Topic frequency and weightage</h2>
<p>Marks share is the average over papers of (topic marks ÷ 100), so every paper counts equally. Frequency, weightage and consistency are separate columns.</p>
{html_table(topic_tbl)}
<img src="../figures/01-pareto-marks-share.png" alt="Pareto of marks share by topic">

<h2>4. Year-wise patterns</h2>
<p>Average marks share, first four vs last three papers (descriptive only; with {n_p} papers no trend test is meaningful):</p><ul>{shift_rows}</ul>
<img src="../figures/02-year-topic-heatmap.png" alt="Year by topic marks share heatmap">

<h2>5. Recurring problem structures</h2>
<p>An archetype is a problem structure (e.g. "find error probabilities for a given critical region"). The most recurrent, by number of papers they appear in:</p>
{html_table(ar_tbl)}
<img src="../figures/05-top-archetypes.png" alt="Top recurring archetypes">

<h2>6. Priority tiers (subtopic level)</h2>
<p>Rule, applied mechanically: <b>Tier 1</b> if the subtopic appears in ≥ {int(stats.TIER1_RATE*100)}% of papers or averages ≥ {int(stats.TIER1_SHARE*100)}% of marks; <b>Tier 3</b> if it appears in &lt; {int(stats.TIER3_RATE*100)}% of papers and averages &lt; {int(stats.TIER3_SHARE*100)}%; else Tier 2. Thresholds sit near the subtopic quartiles; they are a judgement, disclosed here. Counts: Tier 1 = {int((sub.tier=='1').sum())}, Tier 2 = {int((sub.tier=='2').sum())}, Tier 3 = {int((sub.tier=='3').sum())}, untested = {len(untested)}. Tier 3 is "lower historical priority", never "skip".</p>
<h3>Tier 1 subtopics</h3>{html_table(t1)}
<img src="../figures/03-subtopic-appearance.png" alt="Most consistently tested subtopics">
<p>Full tier list for all {len(sub)} subtopics: <code>outputs/tables/subtopics_current.csv</code>.</p>

<h2>7. Potential future areas (hypotheses, not predictions)</h2><div class="hyp"><ul>
<li><b>Hypothesis</b> <span class="ev">strong</span>: {top3.topic.iloc[0]} and {top3.topic.iloc[1]} will stay the heaviest topics; they were heavy in every paper.</li>
<li><b>Hypothesis</b> <span class="ev">moderate</span>: {shift.index[-1]} and {shift.index[-2]} keep the larger share they have had recently, and {shift.index[0]} stays lighter than in {years[0]}–{years[0]+3}.</li>
<li><b>Hypothesis</b> <span class="ev">weak</span>: the subtopics first tested in {years[-1]} keep appearing; the only evidence is one paper ({fresh_marks} marks), so their likely weight is unknown.</li></ul>
<p>Historical frequency is not a probability of appearance. No probabilities are given because {n_p} papers cannot support a defensible model.</p></div>

<h2>8. Preparation recommendations</h2>
<p>Suggested allocation (interpretation): 90% of study time in proportion to historical marks share, and a reserved 10% for the subtopics new to the syllabus ({len(fresh_subs)} first tested in {years[-1]}, where they took {fresh_marks}% of the paper, plus {len(untested)} still untested). Historical shares dilute the new topics because they have one paper of data. Don't drop any syllabus topic for low frequency.</p>
{html_table(alloc)}
<ul><li>Work through past papers <b>by problem structure</b> (Section 5): {pct(near / n_q)} of questions reuse one.</li>
<li>The paper is mostly numerical/application work ({pct(cog.get('numerical', 0) + cog.get('application', 0))}): practise timed computation, not proofs (proof-type questions: {int((cur.cognitive_type == 'proof').sum())}).</li>
<li>Skip ODE-only preparation: not tested since {ode_years[-1]} and not in the 2026 syllabus.</li></ul>

<h2>9. Old-format papers (2012–2014)</h2>
<p>2012 (25 questions, 300 marks, subjective parts), 2013 (30 questions: objective, fill-in-the-blank, descriptive) and 2014 (43 questions incl. 8 descriptive) differ in structure, so they are kept out of all shares above. Heaviest topics there:</p>
{html_table(old[["topic", "questions", "mean_marks_share"]].assign(mean_marks_share=old.mean_marks_share.map(pct)).rename(columns={"topic": "Topic", "questions": "Questions", "mean_marks_share": "Mean marks share"}))}

<h2>10. Methodology and limitations</h2><ul>
<li>Source: official papers from jam2026.iitb.ac.in (SHA-256 manifest). 4 papers are image scans, read with local OCR (PaddleOCR-VL); every page was audited against its image and about 70 OCR errors were fixed. Spot checks still found about 1 meaning-changing OCR slip per 4–5 unchecked pages.</li>
<li>Each question is recorded as number, format, marks and pages, plus a one-line summary (no verbatim text). Counts and marks match each paper's printed instructions, section headers or printed answer key (2016, 2017 and 2022 totals are sums of printed section marks). The validator reports 0 errors on all {len(df)} rows.</li>
<li>Image verification: 2023 and 2024 in full; scans 2014, 2017 and 2025 PASS, but some of their pages were compared against the OCR text rather than the image. Text-based papers 2015–2022 were not sample-verified against images. 2026 (text PDF): every page's OCR compared with its image (5 errors fixed), format and marks match the official answer key, verifier PASS on a 5-page sample.</li>
<li>Topic, archetype, cognitive type and repeat labels are model judgements (subjective). An independent reviewer agreed with 96% of uncertain topic calls (79/82). Archetypes and repeats are <b>moderate evidence at best</b>; cognitive type was not reviewed.</li>
<li>The taxonomy is the 2026 syllabus, while older papers followed earlier syllabi. "Never tested" can mean "newly added".</li>
<li>n = {n_p} papers: everything is descriptive, with no significance tests and no difficulty ratings (no score data).</li>
<li>Reproducible: <code>python -m pyq.master && python -m pyq.report</code> regenerates every table, figure and this report from the frozen data. Code and data: github.com/aaditya19saini/OCR-QP-Tool.</li></ul>
</body></html>"""


def to_pdf(html_path) -> None:
    import subprocess
    pdf = html_path.with_suffix(".pdf")
    subprocess.run(["brave", "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", html_path.as_uri()],
                   check=True, capture_output=True, timeout=120)
    assert pdf.exists() and pdf.stat().st_size > 10_000, "PDF not produced"


def main() -> None:
    log = setup_logging("report")
    verify_manifest()
    df = pd.read_csv(OUTPUTS / "master.csv")
    t = build_tables(df)
    TABLES.mkdir(parents=True, exist_ok=True)
    for k, v in t.items():
        v.to_csv(TABLES / f"{k}.csv", index=k in ("year_topic_share", "format_mix"), float_format="%.4f")
    cur = stats.scope(df)
    figures(t, len(cur), sorted(cur.year.unique()))
    out = OUTPUTS / "report" / "jam_ms_report.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(write_html(df, t))
    to_pdf(out)
    log.info("wrote %d tables, 5 figures, %s (+ .pdf)", len(t), out.relative_to(OUTPUTS.parent))


if __name__ == "__main__":
    main()
