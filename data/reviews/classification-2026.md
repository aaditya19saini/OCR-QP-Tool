# Classification review: JAM 2026 MS (year 15)

Reviewer: classification-reviewer agent, 2026-11-07. Inputs: `data/classified/2026.jsonl` (60 rows, taxonomy `jam-ms-2026-v2`), `data/extracted/2026.jsonl`, OCR `data/ocr/2026/` for Q8, Q11, Q12, Q19, Q25, and the earlier years' extracted + classified rows for every claimed `repeat_of`.
These are **proposals** for the user to decide. No data file was edited. The machine-applicable version is `data/reviews/classification-2026-fixes.json` (same shape as `classification-fixes.json`). All proposed `repeat_of` targets are from earlier years. All proposed topic/subtopic pairs are in `taxonomy.yaml`. The one map target (`classical-counting-probability`) is an existing label that is not itself remapped.

Method: blind tags first, from the summary (plus OCR where the summary was thin), then compared with the existing label.

## 1. Agreement

Reviewed set: the 7 medium-confidence rows plus every row with `repeat_kind` set. 2 rows are medium-confidence only (Q11, Q53), so **n = 41**.

| field | agree | n | rate |
|---|---|---|---|
| topic | 39 | 41 | 95% |
| subtopic | 38 | 41 | 93% |
| cognitive_type | 41 | 41 | 100% |
| archetype | 39 | 41 | 95% |
| repeat (repeat_of + repeat_kind) | 36 | 41 | 88% |

I also checked the topic/subtopic of the 9 null-repeat rows on 2026-syllabus subtopics (section 5): 9/9 agree.

## 2. Disagreements

Strength: **firm** = I'd apply it. **weak** = a judgement call; keeping the current label is defensible.

| uid | field | current | proposed | reason |
|---|---|---|---|---|
| 2026-MS-Q8 | repeat_of | 2022-MS-Q40 (concept) | 2021-MS-Q33 (concept) | firm. 2021-Q33 is the matching root: an N(θ,1) LRT and how its power function behaves. 2022-Q40 is a simple-vs-simple test where power varies with α and δ. Not near: one-sided vs two-sided changes the shape of the power function, which is the whole question. |
| 2026-MS-Q8 | subtopic | Errors, size, power and p-value | Likelihood ratio tests | weak. Consistency: 2021-Q33 and 2020-Q60 (power of a normal-mean LRT) are both filed under LRT. |
| 2026-MS-Q12 | repeat | 2020-MS-Q2 (concept) | null | firm. 2020-Q2 solves for constants that make a piecewise function differentiable. 2026-Q12 is P/Q statements with bounded g, h plus a local-minimum test. The only shared idea is "differentiability of a piecewise function", which is a generic skill. |
| 2026-MS-Q12 | archetype | piecewise-differentiability-constants | piecewise-differentiability-statements (new) | weak, row-level (the label fits 2020-Q2). Nothing is solved for here. Not in the JSON: a map can't express it. Apply by hand or skip. |
| 2026-MS-Q18 | topic/subtopic | Univariate Distributions / Standard discrete distributions | Probability / Axioms and properties of probability | firm. No named distribution is used: the entries are uniform on {-1,0,1} and the work is counting the orthogonal matrices (signed permutations) out of 3^9. Classical counting is filed under Probability / Axioms in this repo (2012-Q7, 2017-Q11, 2022-Q17, 2025-Q50). 2014-Q32 sits under discrete distributions only because its entries are Bin(3,1/3). Keep the near → 2014-Q32 and the archetype. |
| 2026-MS-Q32 | repeat | 2015-MS-Q25 (near) | null | weak. 2015-Q25 is a square singular matrix (det 0). 2026-Q32 is about rectangular m×n matrices: rank of AᵀA and AAᵀ, one-sided inverses. They share the archetype name but not the set-up. Note that 2025-Q13 → 2015-Q25 near was accepted earlier with similar looseness, so if you keep that one, keeping this one is consistent. |
| 2026-MS-Q50 | repeat | 2017-MS-Q56 (concept) | null | firm. P(X₍₃₎ > 1.5) for U(1,2) is the one-line CDF of a maximum. 2017-Q56 is the minimum of exponentials evaluated at μ+σ. The only shared skill is the order-statistic CDF, which is generic. |
| 2026-MS-Q53 | topic/subtopic | Probability / Sample space and algebra of events | Probability / Axioms and properties of probability | firm. Same classical-counting convention as above. |
| 2026-MS-Q53 | archetype | dice-sum-probability | classical-counting-probability | firm. Synonym of the existing label (count the favourable outcomes out of 6⁴). The label is used only once, so the map is safe. |
| 2026-MS-Q55 | repeat_kind | concept (→ 2013-MS-Q29) | near (→ 2013-MS-Q29) | firm on "not concept", weak on near vs null. No specific idea is shared, so concept is the wrong kind. Structurally it is "joint distribution → conditional moment of Y given X = x" with the distribution switched to discrete. That is the same as 2018-Q24 (conditional mean and variance), which is already near → 2013-Q29. If you read pmf vs pdf as a different set-up, use null instead. |

Medium-confidence rows I agree with as they stand: **Q11** (Limit superior and inferior: a definitional tail-sup/inf check, so a separate archetype from `limsup-liminf-of-sequence` is right) and **Q25** (MLE: concept → 2020-Q49 holds. The specific shared idea is MLE invariance for P(X < c) of an exponential).

## 3. Repeat claims: the ones I accept

Near, same set-up with only the numbers or distribution changed: Q1→2024-Q41, Q2→2024-Q42, Q5→2018-Q9, Q7→2016-Q38, Q10→2013-Q7, Q13→2012-Q18.a, Q14→2012-Q5, Q15→2012-Q2, Q18→2014-Q32, Q20→2013-Q25, Q21→2016-Q16, Q22→2015-Q12, Q24→2014-Q33 (both are transformed-gamma scale MLEs: Weibull x³ vs log-gamma eˣ), Q26/Q27→2012-Q15, Q30→2020-Q37, Q31→2017-Q4, Q34→2022-Q34, Q36→2013-Q29, Q37→2022-Q9 (exponential, UMVUE/Rao-Blackwell statements), Q38→2025-Q39, Q41→2019-Q14, Q42→2012-Q16.a, Q45→2016-Q42, Q46→2022-Q23, Q47→2014-Q28, Q48→2017-Q19, Q51→2014-Q17, Q56→2012-Q12, Q57→2012-Q14, Q58→2023-Q50 (sample of 2, p-value through a Gamma(2) sum: a close match).

Concept, with a specific shared idea:
- Q16→2018-Q18: an odd-order skew-symmetric matrix is singular, which is the same fact as "skew-symmetric orthogonal ⇒ n even".
- Q19→2016-Q35: P(A) is a convex combination of P(A|C) and P(A|Cᶜ). 2016-Q35's options turn on exactly this.
- Q25→2020-Q49: see above.

Mild notes (no change proposed):
- Q21 reuses `expectation-from-piecewise-cdf` although the Rayleigh CDF isn't piecewise. The structure (mean from a given CDF) fits, so only the name is narrow.
- All roots are the earliest in their chains. No near-chains were introduced.

## 4. Archetype synonyms

Merge (in the JSON): `dice-sum-probability` → `classical-counting-probability`.

Checked and **kept separate** (similar names, different structure):
- `tail-sup-inf-sequence-limits` (Q11, definitional) vs `limsup-liminf-of-sequence` (compute the limsup of a given sequence)
- `max-order-statistic-probability` (Q50) vs `min-order-statistic-probability`. This follows the earlier split by statistic and by quantity.
- `order-statistic-expectation-of-function` (Q60, middle order statistic) vs `min-order-statistic-expectation`
- `exponential-sum-gamma-properties` (Q40, MSQ distribution facts) vs `gamma-sum-moment` (2023-Q57, one numeric moment). Borderline. Merge them only if you want fewer labels.
- `uncorrelated-linear-combinations` (Q6): no earlier equivalent. `linear-combination-normal-independence` relies on normality.
- `geometric-probability-in-square` (Q44) vs `random-coefficients-geometric-probability`: different set-ups.

Reused labels that fit: `skew-symmetric-matrix-properties` (Q16), `normal-sample-derived-distributions` (Q10, Q30), `error-probabilities-given-critical-region` (Q26, Q27), `marginal-and-conditional-expectation` (Q36, Q55), `random-matrix-property-probability` (Q18). The one that doesn't fit is `piecewise-differentiability-constants` on Q12 (row-level, see table).

Outside 2026 scope, but noticed: `orthogonal-skew-matrix-statements` (2022-Q33) is close to `skew-symmetric-matrix-properties`. I didn't propose a change.

## 5. 2026-syllabus subtopics (sanity)

All filed correctly:
- Descriptive Statistics: Q17 (CV/SD comparison), Q33 (mean, median, mean deviation, range/IQR, scaling) → central tendency and dispersion. Q43 (Spearman correction) → correlation and bivariate data.
- Nonparametric Methods: Q28 (runs test), Q59 (sign test).
- Stochastic Processes: Q9 and Q29 (Markov chains), Q49 (Poisson process).
- Quadratic forms and definiteness: Q3 (definiteness of matrix polynomials from trace and determinant) is correct. Q16 carries it as a secondary concept (xᵀAx = 0), which is right as a secondary.

No missed question: no other 2026 row belongs under those subtopics. One borderline case: Q35 asks for the skewness of Y, but that is distribution skewness from a pdf, not descriptive data, so Univariate Distributions is right. Adding "Moments, skewness and kurtosis" as a secondary concept would be optional. With the fixes applied, new-syllabus marks are unchanged (Q18/Q53 move within the old-syllabus topics).

## Applied (main session, 2026-11-07)
- All JSON changes applied except 2026-MS-Q32 (kept near -> 2015-MS-Q25 for consistency with accepted precedent 2025-MS-Q13; reviewer rated it weak).
- 2026-MS-Q12 archetype `piecewise-differentiability-constants` -> new `piecewise-differentiability-statements` (md-only finding).
