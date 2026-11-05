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
        "topics_2015_2025": topic,
        "subtopics_2015_2025": allsub.sort_values(["questions", "mean_marks_share"], ascending=False),
        "year_topic_share": stats.year_topic(cur, years, "topic", "share"),
        "format_mix": stats.format_mix(df),
        "archetypes_2015_2025": stats.archetypes(cur).reset_index(),
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
    tp = t["topics_2015_2025"].sort_values("mean_marks_share", ascending=False)

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

    st = t["subtopics_2015_2025"]; st = st[st.questions > 0].nlargest(25, "appearance_rate").iloc[::-1]
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
    ax.set_title("Question format mix per paper, 2012–2025 (2012–2014 are old formats)")
    fig.text(0.01, 0.005, "Source: JAM MS papers 2012–2025; top-level questions", fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "04-format-mix.png", dpi=200); plt.close(fig)

    ar = t["archetypes_2015_2025"].head(20).iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.barh(ar.archetype, ar.papers, color=PALETTE[2])
    ax.set_xlabel(f"Papers in which the problem structure appears (of {len(years)})"); ax.tick_params(axis="y", labelsize=7)
    ax.set_title("Most recurring problem structures (archetypes), top 20")
    footer(fig, n_q, years); fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIGS / "05-top-archetypes.png", dpi=200); plt.close(fig)


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
    log.info("wrote %d tables, 5 figures", len(t))


if __name__ == "__main__":
    main()
