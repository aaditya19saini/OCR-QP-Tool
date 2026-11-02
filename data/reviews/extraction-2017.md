# Extraction review — 2017 (MS2017.pdf)

Reviewer: extraction-verifier. Truth: page images `data/pages/2017/p001.png`–`p015.png`. The PDF starts at printed page 2/15 (p001 = notation/useful-data page, no questions); questions are on p002–p014; p015 is the official answer key. OCR text used as a reading aid; flagged pages re-read on the image.

## Verdict

**PASS**: 0 critical, 1 minor.

## Printed totals (for config/papers.yaml)

No instructions page in the PDF. Totals come from the section headers, cross-checked with the answer key:
- **p002:** "SECTION – A, MULTIPLE CHOICE QUESTIONS (MCQ). Q. 1 – Q.10 carry one mark each."
- **p004:** "Q.11 – Q.30 carry two marks each."
- **p008:** "SECTION – B, MULTIPLE SELECT QUESTIONS (MSQ). Q.31 – Q.40 carry two marks each."
- **p011:** "SECTION – C, NUMERICAL ANSWER TYPE (NAT). Q. 41 – Q. 50 carry one mark each."
- **p012:** "Q.51 – Q.60 carry two marks each."
- **p015 answer key:** Section A (MCQ) Q01–30 single key; Section B (MSQ) Q31–40 key sets; Section C (NAT) Q41–60 key ranges. The key prints type and key only, **no marks column**.
- Totals: 10×1 + 20×2 + 10×2 + 10×1 + 10×2 = **100 marks, 60 questions**. Suggested entry: `total_marks: 100`, `expected_questions: 60`, `sections: {A: MCQ, B: MSQ, C: NAT}`, `source: "MS2017.pdf section headers p2, p4, p8, p11, p12; answer key p15 (types)"`. Note: "100" is the sum of the headers, not a printed total.

## Checks

- **Completeness:** Q.1–Q.60 each appear exactly once; 60 records, no gaps, no extras, no subparts.
- **Pages:** Q1–4 p2, Q5–9 p3, Q10–14 p4, Q15–18 p5, Q19–23 p6, Q24–27 p7, Q28–31 p8, Q32–35 p9, Q36–39 p10, Q40–46 p11, Q47–52 p12, Q53–58 p13, Q59–60 p14. All 60 match.
- **Format vs answer key:** Q1–30 MCQ (single letter), Q31–40 MSQ (letter sets), Q41–60 NAT (numeric ranges). All records agree.
- **Marks/section vs headers:** all 60 agree.
- **Summaries:** all 60 checked. No wrong distribution, parameter, statistic or quantity. None states an answer.

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| 2017-MS-Q43 | summary | "Independent normals with different means/variances, U and V averages of groups: compute P(U>V)" | X₁~N(200,8), X₂~N(104,8), X₃~N(108,15), X₄~N(120,15), X₅~N(210,15); U = (X₁+X₂)/2, V = (X₃+X₄+X₅)/3. Summary omits group sizes (2 vs 3) and all parameters | 11 | minor |

## Flags resolved / confirmed

- **Q16 `checked-image`: confirmed.** W = n(ΣXⱼ)² / (m ΣYⱼ²), Xs and Ys iid N(0,1); options are distributions. Summary accurate.
- **Q24 `checked-image`: confirmed** (p7). f(t) = t³(1 + (1/5)cos(logₑ t⁴)) on (0,1], f(0)=0; F(x)=∫₀ˣ f; asks F''(0).
- **Q26 `checked-image`: confirmed** (p7). uₙ = (1+c/n)^{n²} / (3−1/n)^n; asks values of c for convergence. "(root test)" is an extractor label.
- **Q46 `checked-image`: confirmed** (p11). X₁..X₃, Y₁..Y₄ iid N(μ,σ²); k√(15/7)(X̄−Ȳ)/√(pooled SS) ~ t_v; asks v − k.
- No low/medium-confidence records.
