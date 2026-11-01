# Extraction review — 2023 (MS2023.pdf)

Reviewer: extraction-verifier. Truth: page images `data/pages/2023/p001.png`–`p037.png`. I read all 37 pages.

## Verdict

**PASS**: 0 critical, 1 minor.

- **Completeness:** Q.1–Q.60 each appear exactly once in the images. 60 records, no gaps, extras or subparts.
- **Pages:** all 60 `pages` values match the page each question is printed on.
- **Section headers in the images:** p1 "Section A: Q.1 – Q.10 Carry ONE mark each"; p7 "Section A: Q.11 – Q.30 Carry TWO marks each"; p22 "Section B: Q.31 – Q.40 Carry TWO marks each"; p30 "Section C: Q.41 – Q.50 Carry ONE mark each"; p34 "Section C: Q.51 – Q.60 Carry TWO marks each". Every record's `section` and `marks` match these.
- **Format:** Q1–30 have four options with a single answer (MCQ). Q31–40 ask "is/are TRUE" (MSQ). Q41–60 have an answer blank (NAT). All records agree.
- **papers.yaml:** the printed headers give 10×1 + 20×2 + 10×2 + 10×1 + 10×2 = 100 marks over 60 questions, which matches `total_marks: 100` and `expected_questions: 60`. The PDF has no instructions page, so these totals are inferred from the headers. papers.yaml already says so.
- **Summaries:** all 60 checked against the stems. No summary has the wrong distribution, parameter, statistic or quantity.

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| 2023-MS-Q57 | summary | "Independent gammas with scale: Y=X1+2X2+X3 is Gamma; compute E((Y/4)^4)" | X1~Gamma(1,4), X2~Gamma(2,2), X3~Gamma(3,4); asks E((Y/4)^4). The parameters are missing from the summary, so it can't be told apart from similar gamma-sum questions | 36 | minor |

## Flags resolved / confirmed

- **2023-MS-Q5 `stem-as-printed-possibly-typo`: confirmed as printed. Keep the flag.** The page 3 image shows the limit of P((X₁ + X₂ + Xₙ)/4 ≤ x) = G(x), with X₁, X₂, … iid U(0,1), asking for Var(Y), Y ~ G. The options are 1/12, 1/32, 1/48, 1/64. Read literally, the limit is the law of a sum of three iid U(0,1) divided by 4, with variance 3·(1/12)/16 = 1/64. That is option (D), so the printed stem is self-consistent. I can't tell from the paper alone whether the setters meant something else, so I'm not resolving it as a typo. The current summary ("as printed") and `confidence: medium` are accurate.
- No other records carry flags or low confidence.
