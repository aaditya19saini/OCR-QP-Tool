# OCR audit (PaddleOCR-VL output in data/ocr/)

Method per year (dropped-display check added during 2025: a line announcing a formula — 'the matrix', 'given by', 'series', ':' — whose next line has no math): automated checks (question-number sequence ignoring "Q.a – Q.b" range headers; pages < 80 chars; lines repeated > 5x and 20+ char phrase loops; length > 3x median of non-blank pages; MCQ/MSQ blocks with 1–3 of the 4 options; pdftotext question labels and 2+ digit numbers where a text layer exists), visual check of every flagged page, then 2 random unflagged pages (random.seed(year)) compared line by line against the image.

## 2014 (38 pages; no text layer)
- Automated: Q.1–Q.43 contiguous, all MCQs have (A)–(D), no loops.
- Suspicious: p013, p015, p017, p019, p021, p023, p025, p027, p029–p035, p037, p038 (short). Montage checked: all blank answer-space / "Space for rough work" / "DO NOT WRITE ON THIS PAGE" / marks-table pages. OK.
- Spot-check p011, p026: p026 OK. p011 had an error (below).
- Fixes:
  - p004: Q.5 display matrix dropped entirely ("The matrix" followed straight by options) -> inserted `M = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}` from the image. Found by the dropped-display check (added after 2025, run retroactively on 2014/2017/2024).
  - p011: Q.30 vector written as `\dfrac{X}{2}` and density exponent as `x_1^2` -> `\underline{X}` and `x_2^2` (image: X underlined, e^{-x_2^2/2}).
- Note: p036 is the examiner marks table, not content.

## 2017 (15 pages; no text layer)
- Automated: Q.1–Q.60 contiguous, options complete, no loops, no length outliers.
- Note (not OCR): the PDF starts at printed page 2/15 (cover/instructions page absent), and p015 is the official answer key (60 entries, OCR complete).
- Spot-check p004, p008: both match the image. No fixes.

## 2024 (43 pages; no text layer)
- Automated: Q.1–Q.60 contiguous, options complete, no loops. p001 long = instructions page, OK.
- Spot-check p013, p032: p013 OK. p032 had an error (below).
- Fixes:
  - p032: Q.39 option (C) `49S_e^2/\sigma^2` -> `49S_o^2/\sigma^2` (image shows S_o).

## 2025 (62 pages, printed footer x/67; no text layer)
- Automated: Q.1–Q.60 contiguous (the "MCQ1"/"MSQ2"/"NAT1" type labels first tripped the Q-regex; fixed), no loops. p001–p002 long = instructions, OK. Option check flagged p043 (NAT question, "(answer in integer)" false positive).
- Dropped-display check: p044, p037. p037 OK against image. p044 fixed (below). 2024 p028 also flagged (table follows), OCR has the table, OK.
- Spot-check p008, p038: both match the image.
- Fixes:
  - p044: Q.42 power series dropped (watermark behind formula) -> inserted `\(\sum_{n\geq1} \frac{n!}{n^n} x^n\)` from the image.

## 2012 (35 pages; text layer present, old format: 15 MCQ + 10 subjective with (a)/(b) parts)
- Automated: Q.1–Q.25 contiguous, options complete, no loops. Short pages p006–p008, p011–p027 (odd), p029–p034: montage checked, all blank / "Space for rough work". p035 = examiner marks table.
- Text-layer number diffs: p005 (layer artefact, Q.13 checked against image: OK), p009 (answer-grid page, footer only), p028 (OK).
- Added check for 2012 sub-part labels and marks "(9)"/"(12)" vs text layer on the subjective pages p010–p028: p010, p012, p026 missing the "(9)" mark of part (a).
- Spot-check p003, p018 (+ p004 extra, because p003 was badly wrong): p018 OK.
- Fixes:
  - p003: marks note read `\frac{six}{2}` / `\frac{twenty}{2}` -> "six" / "twenty one" (image). Q.3 stem had a fake answer appended and all four options had wrong limits (outer 0..1 limits lost, wrong inner limits) -> rewrote Q.3 stem and (A)–(D) from the image.
  - p004: Q.5 piecewise function rows mangled (sin term split into the condition column, condition of the 0-row wrong) -> `\sqrt{x^2+y^2}\sin(1/\sqrt{x^2+y^2})` if (x,y)≠(0,0); 0 if (x,y)=(0,0).
  - p010: Q.16(a) marks "(9)" missing -> added after "(iii) has no solution."
  - p012: Q.17(a) marks "(9)" missing -> added.
  - p014: Q.18(a) `f(x,y)=x^3+y^3+3x` -> `x^3+y^3+3xy` (image and text layer).
  - p026: Q.24(a) marks "(9)" missing -> added.

## 2013 (35 pages; text layer exists but is itself bad OCR — Greek/operators garbled — so only Q labels were usable)
- Automated: Q.1–Q.30 contiguous, options complete, no loops. Text-layer Q/number mismatches on p002–p005, p007, p010, p014, p024, p028, p031 all traced to the text layer's own garbage (e.g. "n" read as 11, "β" as 13, lost "Q.1" labels), OCR right.
- Short pages p011–p029 (odd), p030–p034: montage checked, blank answer boxes / rough-work pages. p006 = objective answer table, p035 = marks table.
- Spot-check p006, p020 (+ p004 extra, math-heavy): p006, p020 OK.
- Fixes:
  - p004: Q.4 piecewise first row lost its condition (exponential factor pushed into the condition column) -> `\frac{\sin(2(x^2+y^2))}{x^2+y^2} e^{3x\sin(4/y)}, & \text{if } (x,y) \neq (0,0)`.
- New check (run on all done years 2012–2014, 2017, 2024, 2025): every `\begin{cases}` row must have a condition after `&`. No further hits.

## 2015 (18 pages; good text layer)
- Numbering restarts per section: A Q.1–30, B Q.1–10, C Q.1–20 (60 total); sequence otherwise contiguous, options complete, no loops, no short pages.
- Text-layer number diffs p005, p007, p008, p010, p014: all layer artefacts (footer "x/18", section header "Q.11 – Q.30", subscripts like χ²₁₀ read as "102"). OCR right.
- cases check: p005 (notation table) wrote the binomial coefficient as a `cases` block.
- Spot-check (from 2015 on, sampled from pages containing a question, since seed 2015 picked the two instruction pages): p006, p015 both match the image.
- Fixes:
  - p005: binomial coefficient `\begin{cases} n \\ x \end{cases}` -> `\binom{n}{x}` (row is labelled "Binomial coefficient, equal to n!/(x!(n-x)!)").

## Running silent-error tally
Random spot checks so far: 10 pages (2014, 2017, 2024, 2025, 2012), 3 had a meaning-changing math error (wrong subscript/variable/limits) that no automated check catches (2012 extra page p004 also wrong).
