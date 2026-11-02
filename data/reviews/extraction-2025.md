# Extraction review — 2025 (MS2025.pdf)

Reviewer: extraction-verifier. Truth: page images `data/pages/2025/p003.png`–`p062.png` (one question per page). p001 = instructions, p002 = notation; p063–067 not question pages. OCR used as a reading aid; images are the authority.

## Verdict

**PASS**: 0 critical, 1 minor.

## Checks

- **Totals:** p001 instructions: 60 questions, 100 marks; Section A 30 MCQ, Section B 10 MSQ, Section C 20 NAT (already in papers.yaml). Headers: p3 "Section A: Q.1 – Q.10 Carry ONE mark each"; p13 "Section A: Q.11 – Q.30 Carry TWO marks each"; p33 "Section B: Q.31 – Q.40 Carry TWO marks each"; p43 "Section C: Q.41 – Q.50 Carry ONE mark each"; p53 "Section C: Q.51 – Q.60 Carry TWO marks each". 10+40+20+10+20 = 100.
- **Completeness:** Q.1–Q.60 each appear once; 60 records, no gaps/extras/subparts.
- **Pages:** Q_n is on p(n+2) for every n; all 60 `pages` values match.
- **Format/marks/section:** every page carries a type tag (MCQ1, MCQ2, MSQ…, NAT1, NAT2) consistent with the record's format and marks. All 60 agree.
- **Summaries:** all 60 checked. No wrong distribution, parameter, statistic or quantity. Scaled NAT targets are stated (Q49 36P, Q53 V/π, Q58 80δ, Q60 4Cov). None states an answer.

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| 2025-MS-Q56 | summary | "X with E(X)=1, E(X^2)=4, E(X^4)=16: find E(X^3) (equality case of Cauchy-Schwarz/variance of X^2)" | Question gives only the three moments and asks E(X³). The parenthetical is the solution route (Var(X²)=0), not printed text; it points straight at the answer | 58 | minor |

## Flags resolved / confirmed

- **Q7 `checked-image`: confirmed** (p9). Bin(1,p) MLE; claims (I) with √(p(1−p)/n) and (II) with √(p̂(1−p̂)/n); asks which are correct.
- **Q14 `checked-image`: confirmed** (p16). V ⊂ ℝ¹⁰, 10×10 A; options: nonsingular A, singular A with equal dims, rank 8 ⇒ dim A(V) ≥ dim V − 2, equal dims up to A⁵ ⇒ dim A⁶(V) = dim V. Asks which is NOT true. (OCR reads "A^S"; the record's "A^5" is right.)
- **Q21 `checked-image`: confirmed** (p23). X₁..X₅ iid N(0,σ²); c with E(c√ΣXᵢ²) = σ. (OCR reads "X_s"; n = 5.)
- **Q27 `checked-image`: confirmed** (p29). Trinomial with cell probabilities p, 2p, 1−3p, 0 ≤ p ≤ 1/3; properties of MLE p̂.
- **Q48 `checked-image`: confirmed** (p50). f = 1/(xy) on 0<z<y<x<1; asks P(X > 5Y).
- **Q57 `checked-image`: confirmed** (p59). pdf 2θ²x⁻³, x>θ, n=4, X₍₁₎ stated complete sufficient, data 15, 11, 10, 17; UMVUE estimate of θ².
- No low/medium-confidence records.

## Notes

- Many summaries end with extractor-added method labels: Q9 "(chi-square(2)/exponential)", Q21 "(mean of chi distribution with 5 df)", Q24 "(CLT + WLLN, Slutsky)", Q43 "(second-order Taylor)", Q59 "(order statistic via binomial counts)". They are correct and don't give answers, but they're not printed text. Q56 (above) is the one that effectively gives the answer away.
