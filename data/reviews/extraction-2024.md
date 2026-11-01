# Extraction review — 2024 (MS2024.pdf)

Reviewer: extraction-verifier. Truth: page images `data/pages/2024/p002.png`–`p041.png` (all question pages). I read every one. p001 (notations page, via OCR) has no questions. p042–043 (master answer key) were already checked mechanically for format/section/marks and were not re-derived here.

## Verdict

**PASS**: 0 critical, 3 minor.

- **Completeness:** Q.1–Q.60 each appear exactly once in the images. 60 records, no gaps, no extras, no subparts.
- **Pages:** all 60 `pages` values match the page each question is printed on. No question spills onto a second page.
- **Section headers in the images:** p2 "Section A: Q.1 – Q.10 Carry ONE mark each"; p8 "Section A: Q.11 – Q.30 Carry TWO marks each"; p26 "Section B: Q.31 – Q.40 Carry TWO marks each"; p34 "Section C: Q.41 – Q.50 Carry ONE mark each"; p37 "Section C: Q.51 – Q.60 Carry TWO marks each". Every record's `section` and `marks` match these.
- **Format:** Q1–30 have four options and one answer (MCQ). Q31–40 ask "is/are correct" (MSQ). Q41–60 have an answer blank (NAT). All records agree.
- **papers.yaml:** headers give 10×1 + 20×2 + 10×2 + 10×1 + 10×2 = 100 marks over 60 questions, which matches `total_marks: 100` and `expected_questions: 60`.
- **Summaries:** all 60 checked against the stems. None has the wrong distribution, parameter, statistic or quantity. Three are vaguer than they should be (below).

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| 2024-MS-Q26 | summary | "Two independent normal samples: distribution of sqrt5(Xbar+Ybar)/S (t distribution)" | X1..X10 ~ N(3,4), Y1..Y15 ~ N(-3,6), S from the X sample only (divisor 9). The summary leaves out the distributions and sample sizes, so it can't be told apart from other two-sample t questions | 21 | minor |
| 2024-MS-Q52 | summary | "Double integral of 3 sqrt(x^2+y^2)/(sqrt8 pi) over region between y=x and circle radius sqrt8 (polar coordinates)" | ∫₀² ∫ₓ^√(8−x²) … dy dx. The region is the sector between y=x and the y-axis (θ from π/4 to π/2) inside radius √8. "Between y=x and circle" doesn't pin down the region | 37 | minor |
| 2024-MS-Q57 | summary | "Theta ~ U(0,2pi), X=cos Theta, Y=sin Theta: correlation coefficient (uncorrelated but dependent)" | asks for **100ρ** (answer in integer). Other scaled NAT summaries (Q45 8α, Q46 100α, Q48 22E(W), Q49 10E, Q55 12P) give the scale, but this one doesn't | 40 | minor |

## Flags resolved / confirmed

- **2024-MS-Q21 `checked-image`: confirmed.** The p16 image shows X and −X identically distributed, Y = X² with density e^{−y/2}/√(2πy) for y>0, and asks for E((X−1)⁴). The summary is accurate. Note that "(so X ~ N(0,1))" is the extractor's inference, not printed text. It's correct, but per the integrity rules it reads as a solution step.
- **2024-MS-Q46 `checked-image`: confirmed.** The p35 image shows a Cauchy pdf 1/(π(1+x²)), g(x)=x on [−1000,1000] and 0 otherwise, α = lim P(n^{−3/4} Σ g(Xᵢ) > 1/2), asking for 100α. The summary is accurate. Its parenthetical "(…Chebyshev/WLLN, limit 0)" puts the solution inside the summary. I checked it: g(X) is bounded with mean 0, so the variance of the scaled sum is O(n^{−1/2}) → 0 and α = 0. It's correct, but it's an inference rather than a description of what is asked.
- No records have low or medium confidence.

## Notes

- Several summaries tack the method or answer type onto the end in parentheses, e.g. Q8 "n Z_n -> Exp(1)", Q45 "identifies Bin(2,3/4)", Q26 "(t distribution)", Q31 "(ratio test)". The ones I checked are correct. They are labels added by the extractor, not printed text. That matters if summaries are later read as "what the paper says".
