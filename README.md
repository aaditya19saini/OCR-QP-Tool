# OCR-QP-Tool

**A source-traceable question dataset for IIT JAM Mathematical Statistics (2012–2025).**

This repository turns official previous-year papers into structured question records. The goal is to support careful topic and marks analysis while keeping every claim traceable to its paper and page.

> **Project status · 2 November 2026**
>
> Paper inventory, OCR, extraction, classification, and Stage 3 validation are complete. The dataset contains 778 records and currently passes validation with zero errors. The project is paused before statistical analysis; the analysis tables and final report have not yet been produced.

## What’s in the repository

- **14 official papers**, 2012–2025, with a SHA-256 manifest.
- **OCR text** for all 416 pages. OCR is a reading aid; the paper image remains the source of truth.
- **778 extracted and classified records** in JSONL, with page references, formats, marks, summaries, and taxonomy labels.
- **Review notes** documenting OCR audits, image checks, classification decisions, and known limitations.
- **Python pipeline and tests** for inventory, rendering, OCR, validation, master-data generation, and statistics.

The planned deliverables are `outputs/master.csv` and a report PDF. They are not available yet because the statistical-analysis stage has not started.

## Analysis scope

- **Main analysis:** current-format papers from 2015–2025 (60 questions, 100 marks per paper).
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
```

The analysis pipeline uses the project virtual environment. Before committing, run both the test suite and validator as required by [`CLAUDE.md`](CLAUDE.md).

## Pipeline

```text
Official PDFs → rendered pages → local OCR → extracted records
              → classification → validation → master CSV → statistics → report
```

The repository is currently paused after validation. The next approved work begins by applying the reviewed classification fixes, revalidating, and committing that step. Stage boundaries require user approval; do not skip ahead to analysis or reporting.

Useful commands:

```bash
.venv/bin/python -m pyq.render 2023       # render one paper to data/pages/2023/
.venv/bin/python -m pyq.ocr 2023          # OCR selected years (local model required)
.venv/bin/python -m pyq.validate 2023     # validate one year
.venv/bin/python -m pyq.master            # build outputs/master.csv (after approval)
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
| `outputs/` | Generated products; currently includes the paper inventory |
| `docs/guide.md` | Full analysis specification and scope decisions |
| `docs/repo-book.html` | Paginated guide to the repository and contribution workflow |

## Further reading

- [Project instructions and resume plan](CLAUDE.md)
- [Analysis specification](docs/guide.md)
- [OCR audit](data/reviews/ocr-audit.md)
- [Classification review](data/reviews/classification.md)
- [Repository field guide](docs/repo-book.html)
- [Official JAM previous-year papers](https://jam2026.iitb.ac.in/oldQP.html)
