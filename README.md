# OCR-QP-Tool

**A source-traceable question dataset for IIT JAM Mathematical Statistics (2012–2026).**

This repository turns official previous-year papers into structured question records. The goal is to support careful topic and marks analysis while keeping every claim traceable to its paper and page.

> **Project status · 7 November 2026**
>
> Complete. All 15 papers (JAM 2026 added 7 Nov) have been inventoried, OCR'd, extracted, classified and validated: 838 records with zero validation errors. The statistics and the final report are done. **Report: [`outputs/report/jam_ms_report.pdf`](outputs/report/jam_ms_report.pdf)**. Next step: package the method as a generic, exam-agnostic skill.

## Key findings (2015–2026, 12 papers, 720 questions)

- **Statistics is 64.8% of marks, Mathematics 35.2%.** The three heaviest topics are Univariate Distributions (14.5%), Estimation (13.7%) and Multivariate Distributions (10.9%), together 39%.
- **No main topic is skippable.** Each topic tested before 2026 appears in at least 11 of 12 papers, so priorities are set at subtopic level (23 Tier-1 subtopics).
- **The paper is shifting from calculus to distribution theory.** From 2015–2018 to 2024–2026, Integral Calculus fell from 10.2% to 5.0% of marks and Sampling Distributions rose from 3.5% to 7.7%. This is descriptive only (n = 12).
- **44.6% of questions reuse an earlier problem structure** with new numbers. None is a word-for-word repeat.
- **Differential equations disappeared after 2016.**
- **The 2026 syllabus changes showed up in JAM 2026.** 7 subtopics never tested in 2015–2025 (Markov chains, Poisson process, runs and sign tests, descriptive statistics, correlation, matrix definiteness) took 9 questions and 14 of 100 marks. 4 syllabus subtopics are still untested and are flagged as unknown, not low priority.

Methodology, evidence strength and limitations are in the report.

## What’s in the repository

- **15 official papers**, 2012–2026, with a SHA-256 manifest.
- **OCR text** for all 463 pages. OCR is a reading aid; the paper image remains the source of truth.
- **838 extracted and classified records** in JSONL, with page references, formats, marks, summaries, and taxonomy labels.
- **Review notes** documenting OCR audits, image checks, classification decisions, and known limitations.
- **Python pipeline and tests** for inventory, rendering, OCR, validation, master-data generation, and statistics.

Deliverables:
- `outputs/master.csv`: one row per question, with facts and labels.
- `outputs/tables/`: 7 statistics tables.
- `outputs/figures/`: 5 figures.
- `outputs/report/jam_ms_report.pdf` (+ `.html`): the report.

## Analysis scope

- **Main analysis:** current-format papers from 2015–2026 (60 questions, 100 marks per paper).
- **Separate historical note:** 2012–2014, whose paper formats differ. These years are not pooled into current-format marks statistics.
- **Taxonomy:** the official JAM 2026 Mathematical Statistics syllabus. Older questions outside that syllabus are retained and labeled; a topic with no historical appearances is not automatically low priority.

See [`CLAUDE.md`](CLAUDE.md) for the current resume plan and project rules, and [`docs/guide.md`](docs/guide.md) for the analysis specification and scope decisions.

## Quick start

Requires Python 3.12 and `uv`.

```bash
uv venv -p 3.12 .venv
uv pip install -p .venv -r requirements.txt

# Verify the official source PDFs and their manifest
.venv/bin/python -m pyq.inventory

# Validate extracted and classified records
.venv/bin/python -m pyq.validate

# Run the project checks
.venv/bin/python -m pytest -q

# Rebuild every table, figure and the report from the committed data
.venv/bin/python -m pyq.master && .venv/bin/python -m pyq.report
```

The analysis pipeline uses the project virtual environment. Before committing, run both the test suite and validator as required by [`CLAUDE.md`](CLAUDE.md).

## Pipeline

```text
Official PDFs → rendered pages → local OCR → extracted records
              → classification → validation → master CSV → statistics → report
```

Every stage is complete. The report PDF is printed with headless Brave (`brave` must be on `PATH`). Stage boundaries require user approval; see `CLAUDE.md`.

Useful commands:

```bash
.venv/bin/python -m pyq.render 2023       # render one paper to data/pages/2023/
.venv/bin/python -m pyq.ocr 2023          # OCR selected years (local model required)
.venv/bin/python -m pyq.validate 2023     # validate one year
.venv/bin/python -m pyq.master            # build outputs/master.csv
.venv/bin/python -m pyq.report            # tables, figures, report HTML + PDF
```

Rendering and OCR are not needed to inspect the already committed dataset. Local OCR additionally requires the model files and llama.cpp binaries described in `CLAUDE.md` (about 2 GB under `~/.cache/pyq-ocr/`).

## Data integrity rules

- `data/raw/` is immutable. Every pipeline run checks the SHA-256 manifest.
- Never invent question content or marks. Unknown values stay `null` and are flagged; inferences must be labeled.
- OCR is not ground truth. Use the PDF page image to resolve uncertain content.
- Extracted facts and classified judgments live in separate files. Frozen data changes require review and a commit explaining the change.
- Count only top-level questions in paper totals. Subparts remain linked to their parent and are not double-counted.
- Missing is not zero. Use each paper’s own total as the marks-share denominator.
- Historical appearance is descriptive evidence, not a probability that a topic will appear again.

## Repository map

| Path | Contents |
| --- | --- |
| `data/raw/` | Official PDFs and `MANIFEST.sha256` |
| `data/ocr/` | Committed local OCR text |
| `data/extracted/` | Question-level facts (JSONL) |
| `data/classified/` | Topic, archetype, and repeat labels (JSONL) |
| `data/reviews/` | OCR audit, image checks, and classification review |
| `config/papers.yaml` | Paper totals, formats, and cited sources |
| `config/taxonomy.yaml` | Versioned syllabus taxonomy |
| `pyq/` | Pipeline modules |
| `tests/` | Hand-computed and integrity checks |
| `outputs/` | `master.csv`, `tables/`, `figures/`, `report/`, paper inventory |
| `docs/guide.md` | Full analysis specification and scope decisions |

## Further reading

- [Report (PDF)](outputs/report/jam_ms_report.pdf)
- [Project instructions and resume plan](CLAUDE.md)
- [Analysis specification](docs/guide.md)
- [OCR audit](data/reviews/ocr-audit.md)
- [Classification review](data/reviews/classification.md)
- [Official JAM previous-year papers](https://jam2026.iitb.ac.in/oldQP.html)
