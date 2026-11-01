---
name: pdf-extraction
description: Record every question from one JAM MS paper (PDF) into data/extracted/<year>.jsonl from local OCR text (page images as fallback). Use when extracting or re-extracting a paper year.
---

# PDF question extraction (one year per run)

We record **facts and a one-line summary**, not verbatim text. Topic and marks statistics don't need full transcription, and skipping it halves the cost and the error surface.
PDF text layers are unreliable (2014, 2017, 2024, 2025 are scans; Word PDFs mangle math). **Primary input is the local OCR text** `data/ocr/<year>/pNNN.md` (PaddleOCR-VL, LaTeX math; tested exact on 3 pages incl. the 2014 scan). Open the page image only when the OCR looks wrong: garbled math, missing question numbers, a summary you can't write confidently. Record that in flags (`checked-image`). A `pNNN.FAILED.md` means the OCR hit its cap without a clean loop (it can invent content, e.g. extra options (E)-(W)): never use it, always read that page from the image. JAM objective questions have exactly 4 options; more is an OCR fabrication.

## Steps
1. Make sure `data/ocr/<year>/` exists for every page; if not run `.venv/bin/python -m pyq.ocr <year>` (renders pages if needed; ~40 s/page on the local GPU, resumable).
2. Read the instructions page(s). Record `total_marks`, `expected_questions` and `sections` in `config/papers.yaml`, **only if printed**, with `source: "MS<year>.pdf p<N> instructions"`. If they're not printed, leave them null.
3. Read every page's OCR text in order. For each question write one JSON line:
   - `uid`: `<year>-MS-Q<n>`. For independently marked subparts, write a parent row plus child rows `<year>-MS-Q<n>.<a|b|i…>` with `parent_uid` set.
   - `summary`: one line saying what the question asks, specific enough to spot a repeat. Name the distribution, parameters, statistic and what's asked for, e.g. "MLE of θ for U(0,θ) sample of size n; find bias". This is not a transcription.
   - `format`: MCQ | MSQ | NAT | subjective, taken from the section header, never guessed from the content.
   - `marks`: as printed (section header or question). If not printed, `null` plus flag `marks-not-printed`.
   - `section`: as printed, or null.
   - `pages`: 1-based PDF page numbers the question spans.
   - `source_file`: `MS<year>.pdf`.
   - `confidence`: high = fully legible; medium = minor doubt (say which in flags); low = significant doubt.
   - `flags`: short strings, e.g. `illegible:stem`, `numbering-gap`.
4. Skip instructions, blank answer pages and rough-work pages. If you can't tell what a question asks, say so in the summary and set confidence low. Never guess.
5. Write `data/extracted/<year>.jsonl`, sorted by question order.
6. `.venv/bin/python -m pyq.validate <year>`. Fix the errors and review the warnings.
7. Verification: for scans (2014, 2017, 2024, 2025) launch the `extraction-verifier` agent on the full year. For text papers, launch it on 5 randomly chosen pages (seed = year, list them in the report). If the sample finds any critical error, verify the full year. Resolve its findings.
8. Report back: count vs expected, marks sum vs total, flagged items, verifier result. Commit the year (data + review + papers.yaml) and push, then **stop for user approval** before the next year.

## Never
- Infer marks or missing content.
- Merge two questions or split one without the paper's own numbering supporting it.
