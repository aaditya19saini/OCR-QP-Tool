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

## 2016 (18 pages; good text layer)
- Automated: Q.1–Q.60, one gap (Q.50 -> Q.52, Q.52) on p015; options complete, no loops. Remaining number diffs (p004–p009, p014) are missing "x/18" footers or layer subscript artefacts, OCR right.
- p018 is the official answer key (3 side-by-side tables); OCR kept only the first (Q.1–30).
- Spot-check p013, p017: p017 OK, p013 wrong (below).
- Fixes:
  - p015: first NAT two-marker labelled "Q.52" (duplicate) -> "Q.51" (image and text layer).
  - p018: answer key truncated after Q.30 -> appended Q.31–60 rows (type, key, marks) from the image, same format; matches the text layer exactly.
  - p003: Q.8 `Y = \log_x X^{-2\alpha}` -> `\log_e` (text layer "log e").
  - p013: Q.39 option (D) garbled (`2ΣX_i / 2ΣX_i`, χ² term in wrong place) -> `(2ΣX_i/χ²_{2n,α/2}, 2ΣX_i/χ²_{2n,1−α/2})` from the image; stray "(" before "Q.40" removed.

## Cross-year follow-up checks (run after 2016 on all done years)
- Text-layer word check (4+ letter words in the layer missing from the OCR page) on 2015, 2016; marks-header grep ("carry … marks") and a grep for underlined/italic words turned into `\frac{word}{word}` on all done years.
- Fixes:
  - 2013 p003: marks note read `\frac{two}{three}`, `\frac{three}{five}`, `\frac{five}{five}` (underlined words) -> "two", "three", "five" (image). This is the per-section marks statement, so it mattered.
  - 2015 p008: section header "Q. 11 – Q. 30 carry two marks each." missing -> inserted before Q.11 (text layer + footer position).
  - 2015 p007: Q.6 `\Gamma(\alpha, \beta)` population -> `Gamma(\alpha, \beta)` (paper's own notation, text layer "Gamma").

## 2018 (20 pages = 17 question pages + 3-page answer key; good text layer)
- Automated: Q.1–Q.60 contiguous, all 5 marks headers present, options complete, no loops, word check clean. Number diffs = missing "x/17" footers / layer artefacts.
- Answer key p018–p020: 60 rows, keys identical to the text layer.
- cases check: p007, p013; layer-guided look at p003 (OK), p009.
- Spot-check p005, p015: both match the image.
- Fixes:
  - p007: Q.17 sets V, W mangled into a nested `cases` block, column vectors lost x -> rewrote as `V = {(x,y,0) ∈ R^3 : M[x;y;0] = [0;0]}` and `W = {(x,y,z) ∈ R^3 : M[x;y;z] = [0;0]}` (image).
  - p013: Q.38 pdf first row lost its support -> `c(θ) e^{-(x-θ)}, & x ≥ 2θ` (text layer).
  - p009: Q.25 pmf `m+n` -> `\frac{m+n}{21}` (text layer). Q.26 option (A) `&` misplaced inside the density -> `\frac{\sqrt{1/2}}{\sqrt{\pi}} e^{-z/2} z^{-1/2}, & z>0`.

## 2019 (15 pages; good text layer)
- Automated: Q.1–Q.60 contiguous, all 5 marks headers present, options complete, no loops, cases/dropped clean. Number diffs = footers and χ² subscript artefacts (checked p006 Q.21: OCR right).
- Word check: p006 "exist" -> OCR had "exists".
- Spot-check p003, p013: p013 OK, p003 wrong (below).
- Fixes:
  - p003: Q.4 `T([-3;-2])` -> `T([3;-2])` (image; the same vector [3;-2] appears earlier in the stem). Digit-only checks cannot see a dropped minus.
  - p006: Q.17 "If there exists a 3×2" -> "If there exist a 3×2" (wording as printed).

## 2020 (15 pages; text layer has the words but no math glyphs, so number checks are weak)
- Automated: Q.1–Q.60 contiguous, options complete, no loops, cases/dropped clean.
- Marks headers: "Q. 31 – Q. 40" missing (p009). Word check: p007 (Q.21 sentence lost), p009 (that header).
- Spot-check p014, p015: both match the image.
- Fixes:
  - p007: Q.21 "where ε_i' is a data set" (half a sentence dropped) -> "where ε_i's are i.i.d. random variables with mean 0 and variance σ² ∈ (0, ∞). Suppose that we have a data set" (image).
  - p009: section B header "Q. 31 – Q. 40 carry two marks each." missing -> inserted under "MULTIPLE SELECT QUESTIONS (MSQ)" (text layer).

## 2021 (21 pages; good text layer; heavy diagonal watermark)
- Automated: Q.1–Q.60 contiguous, all 5 marks headers present, options complete, no loops. Number diffs: p001/p002 instructions, p011 (below).
- cases check: p010 (set braces written as `cases`). Word check: p005 ("is equal to" dropped).
- Spot-check p012, p016: p016 OK, p012 wrong (below).
- Fixes:
  - p011: Q.26 `a_{n+1} = \frac{1}{3^4}(a_n)^{3/4}` -> `3^{\frac{1}{4}} (a_n)^{\frac{3}{4}}` (image).
  - p010: Q.(critical region) `R = \begin{cases} … \end{cases}` -> `R = \left\{ … \right\}` (a set, not a piecewise function).
  - p005: Q.9 "is equal to" after P(Urn 1 is selected | …) missing -> added (text layer).
  - p012: Q.30 option (B) `P(E_2 ∩ E_3) ≤ 2/5` -> `≤ 1/2` (text layer; the watermark crosses this fraction in the image).

## 2022 (44 pages, footers x/52; good text layer; one question per page in tables)
- Automated: Q.1–Q.60 contiguous, all 5 marks headers present, no loops. Number diffs = footers and σ²/x² subscript artefacts (p033, p042 checked: OCR right). p038 option flag = NAT false positive.
- cases check: p006. Word check: p001 (notation table), p030 ("nonsingular"), p038 (layer artefact "limsupn", OCR right).
- Spot-check p022, p032: both match the image (p022 had an unclosed `\[`, closed).
- Fixes:
  - p006: Q.7 joint pdf first row lost its support (`&` inside the density) -> `\dfrac{\sqrt2}{\sqrt\pi} e^{-2x} e^{-(y-x)^2/2}, & 0<x<∞, -∞<y<∞` (text layer).
  - p001: notation rows shifted: χ²_n symbol glued to the Φ row, F_{m,n} given the chi-square description, Snedecor F row lost -> rebuilt the Φ, χ²_n, F_{m,n}, t_{n,α} rows from the text layer.
  - p030: Q.(C) "non-singular" -> "nonsingular" (as printed; cosmetic).
  - p022: closed the display `\[ … \]` (cosmetic).

## 2023 (37 pages; native text layer, very good; OCR output was the weakest of all years)
- Done-check: 34 pNNN.md + 3 pNNN.FAILED.md (pipeline flagged as truncated / not a clean loop).
- Because the layer is native and OCR quality was poor, I compared every page against the text layer, and checked the image wherever the layer's stacked fractions/limits were ambiguous (twice the layer was wrong and the OCR right: p028 Q.38(D) limits and Q.39(A) 4/√15).
- After fixes: Q.1–Q.60 contiguous, all 5 marks headers present, cases/dropped/word checks clean.
- Fixes:
  - p005: OCR failed (invented options (E)–(W) after the real four, truncated) -> written from image + text layer (Q.8, options (A)–(D) only).
  - p012: OCR failed (truncated; condition −1 ≤ x ≤ 1 had also drifted outside the cases block) -> written from image + text layer (Q.17).
  - p017: OCR failed (truncated after (C)) -> written from image + text layer (Q.22).
  - p001: Q.1 option (B) `x \cup z = 0` -> `x + z = 0`.
  - p003: Q.5 label missing and "Then, Var(Y) equals" dropped -> added both.
  - p004: Q.7 label, f(x,y) = 2x² − xy − 3y² − 3x + 7y and "the point (1, 1) is" all dropped -> added.
  - p006: Q.10 pdf `f(x;θ) = (3−θ)x^{2−θ} if 0<x<1; 0 otherwise` dropped -> added.
  - p007: Q.11(B) `χ²` -> `χ²_2`.
  - p008: Q.13 "will be less than 2, equals" dropped -> added.
  - p009: watermark text ("Joint Admission test for Masters / Organizing Institute / …", 7 lines) transcribed as content -> removed.
  - p010: Q.15 "i, j, d" -> "i.i.d."; the α₂ = lim P(|S_n − 1/3| < 1) line dropped -> added.
  - p015: Q.20(D) `≠` -> `=`.
  - p016: Q.21(D) `Var(Y | X) = 1/2 = 1/12` -> `Var(Y | X = 1/2) = 1/12`.
  - p019: Q.26 option (A) `16π` (duplicate of B) -> `16π − 16`; "is" added before options.
  - p020: Q.28 label missing -> added.
  - p021: Q.29 `\Gamma \Gamma \Gamma \Gamma (2, 1/2)` -> `Gamma(2, 1/2)`.
  - p025: Q.34(C) `Cov = 5/3` -> `−5/3` (image).
  - p027: Q.37 `U = x/Y` -> `X/Y`, `E(e^{tz})` -> `E(e^{tZ})`.
  - p030: Q.42 "i, i. d." -> "i.i.d.".
  - p031: Q.44 estimator `X = c/10 Σ|X_i|` -> `Y = …`; Q.45 `ln(2/x)` -> `ln(2/X)`.
  - p032: Q.47 `n ≥ 2, 3, …` -> `n = 2, 3, …`; Q.48 `(1+k)/4^{k−1}` -> `(1 + k 2^k)/4^{k−1}` (image).
  - p034: Q.51 `· x ∈ R` -> `, x ∈ R`; Q.53 integrand dropped `∫_{-∞}^{∞} dx` -> `∫_0^∞ 2^{−x²} dx` (image).
  - p035: Q.54 pdf `&` misplaced / support lost -> `x/θ² e^{−x/θ}, & if x > 0`; "then" -> "Then"; Q.55 pmf `θ(1, θ)^x, & otherwise` -> `θ(1−θ)^x, & if x = 0,1,2,…`; `\hat{t}` -> `\hat{\tau}`.
  - p036: Q.58 set R written as `cases` -> `\left\{ … \right\}`.
- Spot-check: n/a (all 37 pages compared).

## Cross-year checks added at the end (run on all 14 years)
- Option labels beyond (D) / questions with >4 options (invented-content check requested by the main session): only hit was 2021 p004 (a stray repeated option) and 2023 p003/p004/p020 (missing Q labels merged two questions). No (E)+ labels anywhere after the 2023 FAILED rewrites.
- Duplicate option text inside one question: 2016 p005, 2017 p010, 2023 p019 real; 2021 p014, 2022 p004, 2024 p027, 2025 p015 false positives (shared prefixes).
- Word check extended to count "equal(s)/then/where/limit" (a dropped "is equal to" now shows).
- Fixes:
  - 2021 p004: Q.4 limit dropped -> `\lim_{n→∞} \sum_{k=0}^{n} \binom{2n}{k} \frac{1}{4^n}` (image); Q.5 a stray "(D) Φ(2)" in place of "is equal to" -> replaced with "is equal to".
  - 2017 p010: Q.37 option (B) `(X_1²+X_2²)/2` (duplicate of C) -> `(X_1²+X_2)/2` (image).
  - 2016 p005: Q.14 option (D) `e^{−e^{−2}}` (duplicate of C) -> `e^{−e^{2}}` (image).

## Running silent-error tally
Random spot checks (2 per year, 13 years; 2023 compared in full instead): 26 pages, 6 had a meaning-changing error that no automated check caught (2014 p011, 2024 p032, 2012 p003, 2016 p013, 2019 p003, 2021 p012) = ~23% of pages. The 3 extra math-heavy pages I looked at (2012 p004, 2013 p004, and the 2023 full pass) agree. Most errors are a single wrong subscript, sign, limit or fraction inside otherwise-correct text, often where a watermark crosses the formula. Expect similar residual errors on the pages nobody has looked at by eye, mostly in years without a usable text layer (2014, 2017, 2024, 2025) and 2013 (garbage layer).

## OPEN
- None illegible. Residual risk: unchecked pages in no-layer years (2014, 2017, 2024, 2025) and 2013 likely still hold ~1 subtle math error per 4–5 pages. Question numbers, option counts, marks headers and answer keys are verified for all years.

## 2024 follow-up (main session, during extraction)
- p016: Q.21 density g(y) mangled (fraction split across case rows) -> `e^{-y/2}/\sqrt{2\pi y}` if y>0, 0 if y<=0 (image).
- p035: Q.46 `\frac{1}{n^4} - \sum` -> `\frac{1}{n^{3/4}} \sum` (image).

## 2026 (added 2026-11-07, main session; full image comparison of all 47 pages)
Source: MS2026.pdf (text layer present, JAM 2026 watermark on every page). Local OCR, 47 pages, no FAILED pages, no loops.
Every page's OCR was compared against its rendered image (data/pages/2026/pNNN.png) by eye.
- Meaning-changing errors (fixed from image):
  - p004 Q.4: options (B), (D) came out as empty fractions `\frac{y^{3/4}}{}`, `\frac{y^{1/4}}{}` -> `y^{3/4}`, `y^{1/4}`.
  - p023 Q.24: density exponent split, `e^{3x} - e^x/β` -> `e^{3x - e^x/β}`.
  - p024 Q.25: `(log_e 2)^T` (power) -> `(log_e 2)T` (product).
- Content dropped by OCR (added from image, marked in the file):
  - p008 Q.9: Markov chain transition diagram (1→1 0.25, 1→2 0.75, 2→1 0.5, 2→2 0.5).
  - p028 Q.29: 3x3 transition matrix [[1/2,1/4,1/4],[0,1/5,4/5],[0,1,0]].
- Minor, not fixed (meaning recoverable): p001 ℕ/ℝ as N/R; p011 mismatched `\[ ... \)`; p018 "SI" for "S1"; p019 watermark text "IIT BOMBAY" in output; p025 subscript `0,0143` for 0.0143; p031 "Page.31"; p045 Q.55 "0, otherwise" row duplicated/jumbled (formula and support intact).
- Clean: the other 39 pages match exactly.
- Tally: 5/47 pages (11%) had a substantive error, lower than the ~23% seen on older papers (clean typeset source).
