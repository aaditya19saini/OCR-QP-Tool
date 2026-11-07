# JAM MS PYQ Intelligence

Analysis of IIT JAM Mathematical Statistics previous-year papers. **The spec is `docs/guide.md`, as narrowed by "Scope decisions" below (which win on conflict). Read both before any stage.**
The goal is a statistically honest report that helps a student allocate preparation time.

## Stage gate (mandatory)
The stages are: 1 inventory → 2 extraction → 3 validation → 4 statistics → 5 interpretation → 6 report.
- After each stage (and after each year batch in extraction), stop. Give a short progress summary and list unresolved issues.
- Wait for the user's approval before starting the next stage.
- Never jump ahead to reporting.

The user explicitly allowed (2026-11-01): commit and push every finished step to https://github.com/aaditya19saini/OCR-QP-Tool (public), and run extraction for the remaining years in parallel agents. Still stop for approval between stages.

## Current state and resume plan (updated 2026-11-02)
Done and pushed (last commit "Checkpoint (agents paused by user)"):
- Stage 1: 14 official papers 2012–2025 in `data/raw/` (2013, 2016 and 2019 added from jam2026.iitb.ac.in/oldQP.html).
- OCR: all 416 pages in `data/ocr/`, audited against images (`data/reviews/ocr-audit.md`, about 70 fixes). Spot checks found about 1 meaning-changing error per 4–5 unchecked pages, so OCR is a draft, not ground truth.
- Syllabus: `docs/syllabus/syllabus_MS_JAM2026.pdf` (fetched with user approval) → `config/taxonomy.yaml` v `jam-ms-2026-v1` (15 topics, 76 subtopics).
- Extracted: all 14 years, 778 rows (45+30+43+11×60), validator 0 errors. Verified against images: 2023 and 2024 (PASS).
- Classified: all 14 years (taxonomy v2).
- Analysis code ready and tested: `pyq/master.py`, `pyq/stats.py` (25 tests pass).

**2026-11-07: JAM 2026 added as year 15 and fully integrated.** Raw + manifest, OCR (all 47 pages image-checked, 5 fixed), extraction (verifier PASS), classification (reviewer: `data/reviews/classification-2026.md`, fixes applied except Q32). Main scope is now **12 current-format papers 2015–2026** (720 Q); report, README and `docs/resources.md` regenerated/updated. Tables renamed `*_current.csv`. New finding: 7 subtopics first tested in 2026 (9 Q, 14 marks); 4 still untested.

**2026-11-05: Stages 4–6 DONE. Report at `outputs/report/jam_ms_report.pdf` (+ .html), tables in `outputs/tables/`, figures in `outputs/figures/`; regenerate with `python -m pyq.master && python -m pyq.report`. Remaining: step 7 (generic exam-agnostic skill), optional text-paper sample verification.** Optional open item: 5-page sample verification of the 10 text papers (counts/marks are already confirmed; only summaries are unchecked there).

Resume in this order (progress 2026-11-02):
1. ~~Classify 2014–2022~~ DONE. All 14 years classified.
2. ~~Printed totals in papers.yaml~~ DONE for all 14 (2016, 2017, 2022 inferred as sums of printed section marks, labelled INFERRED).
3. ~~Image-verify the scans 2014, 2017, 2025~~ DONE: all PASS, 0 critical (`data/reviews/extraction-<year>.md`). Caveat: many scan pages were compared against OCR, not images. Text-paper 5-page samples: NOT done (optional).
4. ~~Taxonomy gap~~ DONE: taxonomy v2 adds "Differential Equations (pre-2026 syllabus)"; 11 ODE rows re-filed. ODEs appear only 2012–2016, which is a finding for the report.
5. ~~Archetype merge + repeat tightening~~ DONE: 414→367 archetypes; repeats are structure-level (user decision 2026-11-02): near = same problem structure + set-up (297), concept = specific shared idea (20), 0 exact. Report them as "repeated problem structures". Was: It writes `data/reviews/classification.md` and machine-applicable `data/reviews/classification-fixes.json` ({archetype_map, repeats, topics}); apply mechanically, revalidate, commit. Workers flagged 30–38 of 60 questions per year as repeats (too generous).
6. **Stage 3 summary, then stop for approval.** Then the analysis plan (agreed with user 2026-11-02):
   - Scope: main analysis = the 11 current-format papers **2015–2025** (60 Q / 100 marks). 2012–2014 (300 marks / subjective / 43 Q) get a separate old-format note, never pooled.
   - a. Apply the reviewer fixes (`data/reviews/classification-fixes.json`), revalidate, commit. This blocks the rest.
   - b. `python -m pyq.master` → `outputs/master.csv`.
   - c. Sanity asserts before using any number: topic marks per paper sum to 100; top-level counts = expected_questions; no subparts in totals.
   - d. Tables from `pyq/stats.py`: topic table (frequency, marks share, appearance rate over 11 papers, recent = last 3, # archetypes), subtopic table (detail only, small n), year × topic marks matrix, format mix per year, top archetypes by # papers with example uids, tiers (rule in code).
   - e. Five figures (Pareto of marks share, year × topic heatmap, appearance rate, format mix, top archetypes), each with a source + n footer.
   - f. Interpretation: numbers only from the tables; each finding tagged strong / moderate / weak evidence; future areas = hypotheses, no probabilities.
   - g. Report HTML → PDF (headless Brave) + `master.csv`; commit and push.
   - Known findings to state: ODEs disappear after 2016 (don't prepare them). 2026-syllabus topics rarely or never tested before (descriptive statistics, nonparametric methods, stochastic processes) may be new, so flag them separately and don't rank them low. n = 11, so describe trends; don't test them.
   - Skip: Excel, significance tests, difficulty, concept map, the guide's other 7 figures. New code: only a small `pyq/report.py`.
   - Caveats for the limitations section: repeat/archetype results are moderate evidence at best. Some scan summaries were checked against OCR, not images; this affects archetypes, not counts/marks/topics.
7. **After the first full run (user request, 2026-11-02):** package the proven pipeline as a generic, exam-agnostic skill ("PYQ analytics from any exam's papers + syllabus"): inventory/manifest → local OCR with loop/fabrication guards → OCR audit → extraction with printed-answer-key cross-check → versioned taxonomy from the syllabus → classification → validation → stats → report. Exam-specific facts (formats, eras, quirks) go in a per-exam config, not in the skill. Build it only from steps that actually ran.

## Per-paper quirks (read before touching a year)
- **2012:** old format, 25 Q, 300 marks (p1). Q1–15 MCQ at 6 marks; Q16–25 subjective at 21 marks with child rows (a)=9, (b)=12. No section labels. Era "old".
- **2013:** 30 Q, 100 marks (p1). Sections "Objective" (Q1–10 MCQ, 2 marks), "Fill in the blank" (Q11–20, 3 marks, stored as NAT with flag `printed-format:fill-in-the-blank`), "Descriptive" (Q21–30 subjective, 5 marks). Era "old".
- **2014:** image scan, 43 Q, older format. Era "old".
- **2015:** questions printed per section ("C.Q20"); stored as Q1–60 with flag `printed-as-...`.
- **2016, 2017, 2018, 2024:** the PDF prints an official answer key (type, marks, key). Cross-check format and marks against it. Keys are not used for anything else (scope decision).
- **2017:** image scan, no printed page 1.
- **2023:** no instructions page; totals come from the section headers. Heavy "JAM 2023" watermarks broke OCR (loops, invented options); 3 pages were rewritten from images.
- **2024, 2025:** image scans. 2024 matched its answer key exactly.
- Era rule (`pyq/master.py`): "current" = 60 Q / 100 marks in papers.yaml, else "old". Old-era papers are reported separately.

## Lessons (don't relearn these)
- Local OCR (PaddleOCR-VL) can **invent content** under watermarks, e.g. extra options (E)–(W). JAM objective questions have exactly 4 options; more is fabrication. `pNNN.FAILED.md` = never use, read the image.
- Parallel workers must not edit `config/papers.yaml` or use git. They report totals; the main session applies them and commits.
- Summaries describe the question, never its answer.

## Scope decisions (override guide.md; agreed with user 2026-11-01)
- **No verbatim transcription.** Extraction records facts (number, format, marks, pages) plus a one-line `summary` of what each question asks. Page images are the reference for anything deeper.
- **No difficulty field.** There are no score data, and answer keys exist only inside 4 PDFs (2016–2018, 2024), so difficulty would be a guess. Keys are used only to cross-check format and marks.
- **No significance or trend tests.** 14 papers is too few. Describe the year-by-topic pattern plainly.
- **Deliverables: `outputs/master.csv` + one report PDF** (HTML printed via headless Brave), with methodology and limitations inside the report. No Excel workbook, no separate methodology doc.
- **2012 (and any other old-format paper) is reported separately**, never pooled into the main weightage or trends.
- **Agents:** extraction-verifier on full scans, sampled pages on text papers; classification-reviewer on uncertain items and repeat claims only. Stats are checked by tests, not by an auditor agent.

## Data integrity rules (guide §14, non-negotiable)
1. Never fabricate exam data. Never infer missing marks, years, question numbers or text. Use `null`, add a flag, and move on.
2. Any inference must be labelled as an inference.
3. Every statistic must be recomputable from `outputs/master.csv`. Every question traces to file + page.
4. Topic marks must sum to the paper totals. Never double-count: totals use top-level questions, and subparts are kept as separate rows linked by `parent_uid`.
5. **Missing is not zero.** All 14 years 2012–2025 are present, but null fields (unprinted marks, unread pages) are missing, never 0. If a year is ever absent it is a gap on every axis.
6. Denominators: percentages use each paper's own total. The main analysis covers current-format papers only; old-format papers get their own note.
7. Show n next to every important statistic. With 14 papers, don't overstate.
8. No appearance probabilities or confidence percentages without a defensible model. Future-topic statements are labelled **hypotheses**.
9. Keep objective facts (`data/extracted`) separate from subjective judgements (`data/classified`). Archetype and cognitive type are subjective.
10. "Repeated" means the same question, or the same structure with changed numbers. Same topic alone is not a repeat.
11. Only use the papers and the official syllabus (JAM 2026 version, fetched with user approval). No other external sources unless the user asks. The syllabus is the 2026 version: topics with zero past questions may simply be new to it, so never call them "low priority" on that basis alone.

## Directory contract
| Path | Rule |
|---|---|
| `data/raw/` | **Immutable.** PDFs and MANIFEST.sha256 are read-only. Every script checks the manifest first. |
| `data/extracted/<year>.jsonl` | Claude-read question index, **frozen** once validated and committed. Fix it with a reviewed edit, never a silent regenerate. |
| `data/classified/<year>.jsonl` | Claude classification, frozen the same way. |
| `data/reviews/` | Subagent findings, one file per review. |
| `data/ocr/<year>/` | Local OCR text, committed (hours to regenerate). Primary extraction input. |
| `data/pages/`, `logs/*.log` | Regenerable and gitignored. |
| `config/papers.yaml` | Per-paper totals, filled only from the paper's own instructions page, with `source` cited. |
| `config/taxonomy.yaml` | Syllabus taxonomy. Bump `version` on any change. |
| `outputs/` | Deterministic products of the frozen data. |

Claude is the only non-deterministic step. Everything downstream is plain Python that gives the same output for the same inputs: sorted, no timestamps in data files.

## Record schema (enforced by `pyq/validate.py`, which is the source of truth)
- **extracted:** `uid` (`2023-MS-Q12`, subpart `2012-MS-Q3.b`), `parent_uid`, `year`, `section`, `format` (MCQ|MSQ|NAT|subjective), `marks` (int or null), `summary` (one line: what is asked), `source_file`, `pages` (1-based PDF pages), `confidence` (high|medium|low), `flags` (list of strings)
- **classified:** `uid`, `subject`, `topic`, `subtopic` (all must exist in the taxonomy), `secondary_concepts`, `cognitive_type`, `archetype`, `repeat_of`, `repeat_kind` (exact|near|concept|null), `confidence`, `rationale`, `taxonomy_version`

## Commands
Always use the project venv (Python 3.12):
```
.venv/bin/python -m pyq.inventory          # stage 1, verifies manifest
.venv/bin/python -m pyq.render 2023        # pages → data/pages/2023/*.png + text dump
.venv/bin/python -m pyq.ocr [years]        # local PaddleOCR-VL → data/ocr/<year>/pNNN.md (GPU, resumable)
.venv/bin/python -m pyq.validate [years]   # exit 1 on any error
.venv/bin/python -m pyq.master             # join extracted + classified → outputs/master.csv (fails if any question unclassified)
.venv/bin/python -m pytest -q              # run before every commit
```
Recreate the env: `uv venv -p 3.12 .venv && uv pip install -p .venv -r requirements.txt`
OCR tools (not in git, ~2 GB): `~/.cache/pyq-ocr/` = llama.cpp b12032 CUDA 13.4 build (`llama-cuda/`, uses the RTX 3050, ~6 s/page) with Vulkan build fallback (`llama/`, iGPU only, ~45 s/page) + `PaddlePaddle/PaddleOCR-VL-1.6-GGUF` files (model, mmproj, chat_template.jinja) from Hugging Face.

## Skills and agents
| When | Use |
|---|---|
| Indexing a paper's questions | skill `pdf-extraction` |
| Tagging topics, archetypes, repeats | skill `question-classification` |
| Checking a dataset or totals | skill `data-validation` |
| Computing stats, patterns, tiers | skill `statistical-analysis` |
| Figures and the report PDF | skill `report-generation` |
| After each extracted year | agent `extraction-verifier` |
| After classification (uncertain items only) | agent `classification-reviewer` |

## Code conventions
- Put new code in its stage module only when that stage starts. No stubs.
- Use `pyq.common` for paths, `setup_logging(stage)` (logs a run header with git sha, manifest hash and versions), `verify_manifest()` and `IntegrityError`.
- Fail loudly on integrity problems. Don't catch-and-continue.
- Non-trivial logic gets a test in `tests/`. Stats functions are tested on hand-computed fixtures; that is the stats audit.
- Commit frozen data and config changes with a message saying what changed and why.
