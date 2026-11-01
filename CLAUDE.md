# JAM MS PYQ Intelligence

Analysis of IIT JAM Mathematical Statistics previous-year papers. **The spec is `docs/guide.md`, as narrowed by "Scope decisions" below (which win on conflict). Read both before any stage.**
The goal is a statistically honest report that helps a student allocate preparation time.

## Stage gate (mandatory)
The stages are: 1 inventory → 2 extraction → 3 validation → 4 statistics → 5 interpretation → 6 report.
- After each stage (and after each year batch in extraction), stop. Give a short progress summary and list unresolved issues.
- Wait for the user's approval before starting the next stage.
- Never jump ahead to reporting.

Current state: stage 1 done (14 papers, 2012–2025). 2023 extracted and verified. OCR of all papers running/done in `data/ocr/`. Taxonomy waits on the official syllabus PDF in `docs/`.

## Scope decisions (override guide.md; agreed with user 2026-11-01)
- **No verbatim transcription.** Extraction records facts (number, format, marks, pages) plus a one-line `summary` of what each question asks. Page images are the reference for anything deeper.
- **No difficulty field.** There are no answer keys or score data, so it would be a guess.
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
11. Only use the papers and the official syllabus. No external sources unless the user asks.

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
