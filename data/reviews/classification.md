# Classification review: archetypes, repeats and topics (all 14 years)

Reviewer: classification-reviewer agent, 2026-11-02. Inputs: `data/classified/*.jsonl` and `data/extracted/*.jsonl` (778 rows, taxonomy `jam-ms-2026-v2`).
These are **proposals**. No data file was edited. The machine-applicable version is `data/reviews/classification-fixes.json`. A script checked it: every uid exists, every topic/subtopic is in `taxonomy.yaml`, every `repeat_of` is from an earlier year, no near-chains are left, and every map target is a real label that is not itself remapped.

Note: CLAUDE.md says 837 extracted rows, but there are 778 in both `extracted/` and `classified/`. That is worth a recount before stats.

## 1. Archetype merge

- **Before: 414 labels. After: 368** (46 labels mapped into 34 canonical labels).
- Rule: merge only when the problem set-up is the same. Pick the most-used label, or the clearer one when it's a tie or the most-used name misleads (e.g. `mp-test-exponential-chisq-cutoff` also covers beta and Laplace items, so the general name wins).

| canonical | merged in |
|---|---|
| error-probabilities-given-critical-region | error-probability-discrete-test, error-probabilities-given-test-continuous, type-i-ii-error-binomial-test, size-power-given-critical-region, size-of-test-uniform-max, power-chi-square-variance-test, power-normal-two-sample-test |
| classify-critical-point-two-variables | classify-critical-points-two-variables |
| parametric-linear-system-consistency | linear-system-parameter-solutions |
| mp-test-cutoff-via-chi-square | mp-test-exponential-chisq-cutoff |
| mp-test-rejection-region-form | mp-critical-region-form |
| mgf-identify-distribution | joint-mgf-independent-binomials, moments-identify-distribution |
| normal-sample-derived-distributions | identify-sampling-distribution |
| eigenvalues-of-matrix-function | trace-of-matrix-function-from-eigenvalues |
| two-variable-differentiability-at-origin | continuity-partials-at-origin, partial-derivative-existence-at-point |
| leibniz-rule-derivative-value | leibniz-rule-derivative, leibniz-rule-derivative-evaluation |
| umvue-identify-formula | umvue-of-parametric-function, complete-sufficient-umvue-reciprocal |
| regression-estimates-from-sums | regression-coefficients-from-moments, regression-prediction-from-sums |
| series-convergence-implications | series-convergence-statements, derived-series-convergence |
| joint-pdf-covariance | joint-pdf-marginals-independence-covariance |
| limit-as-derivative-definition | limit-as-derivative |
| riemann-sum-limit | limit-as-riemann-sum |
| cayley-hamilton-matrix-equation | cayley-hamilton-identify-matrix-equation |
| chi-square-pivot-confidence-interval | chi-square-pivot-ci-constant |
| rank-of-given-matrix | matrix-rank-computation |
| linear-map-from-basis-images | linear-map-on-basis-coordinates |
| function-injective-surjective-check | injectivity-surjectivity-of-function |
| mle-uniform-location-nonunique | mle-uniform-location-non-unique |
| constant-for-unbiased-estimator | constant-for-unbiased-scale-estimator |
| f-reciprocal-quantile | f-reciprocal-probability |
| log-uniform-to-chi-square | transformation-to-exponential |
| piecewise-pdf-interval-probability | piecewise-pdf-probability |
| pmf-from-constraints | pmf-normalising-constant |
| binomial-of-binomial-probability | binomial-no-defectives |
| parameter-from-pmf-relation | binomial-parameter-from-pmf-ratio |
| sum-of-geometrics-negative-binomial | negative-binomial-tail-probability |
| conditional-probability-inequalities | conditional-probability-statements |
| inclusion-exclusion-at-least-k-events | inclusion-exclusion-union-probability |
| classical-counting-probability | combinatorial-probability-pairs |
| moment-existence-check | finite-expectation-check |

**Deliberately kept separate** (similar names, different structure): mle-closed-form vs mle-numeric-estimate; umvue-identify-formula vs umvue-numeric-estimate; consistency-of-estimators vs unbiased-consistent-check-of-estimator; mp-test-cutoff-single-observation (no chi-square) vs mp-test-cutoff-via-chi-square; lagrange-extrema-on-circle vs nearest-point-on-surface; moment-from-mgf (differentiate an MGF) vs mgf-identify-distribution; type-ii-error-normal-mean-test (cutoff comes from the size) vs error-probabilities-given-critical-region (cutoff is given); min-order-statistic-expectation vs -probability; transformation-to-chi-square vs log-uniform-to-chi-square.

**Row-level archetype fixes** (a label map can't express these, because the label is right for its other rows). Apply by hand:

| uid | current | proposed | why |
|---|---|---|---|
| 2016-MS-Q42 | markov-inequality-bound | chebyshev-inequality-bound | the summary asks for a Chebyshev bound |
| 2013-MS-Q6 | clt-limit-of-probability | clt-approximate-distribution-of-sum | asks for a limiting distribution, the same as 2020-Q9 |
| 2015-MS-Q51 | marginal-and-conditional-expectation | iterated-expectation-hierarchical | E(X) through X\|Y in a hierarchy |
| 2022-MS-Q60 | p-value-computation | t-test-normal-mean | p-value of a one-sample t-test, the same as 2023-Q28 |
| 2014-MS-Q39 | sum-difference-of-normals | normal-linear-combination-probability | probability of a linear combination of independent normals |
| 2025-MS-Q17 | sum-difference-of-normals | linear-combination-normal-independence | the same set-up as 2022-Q36 |

Nine near-pairs in the fixes file cross these labels (2017-Q12, 2019-Q46, 2020-Q7, 2022-Q20 → 2016-Q42; 2019-Q48, 2022-Q7 → 2015-Q51; 2020-Q9 → 2013-Q6; 2023-Q28, 2024-Q10 → 2022-Q60). They become consistent once the row fixes are applied.

## 2. Repeat claims

Rule as applied:
- **near** = same canonical archetype AND same set-up, with only the numbers, function or distribution changed.
- **concept** = only a *specific* non-generic idea is shared (e.g. weighted-mean estimator inconsistency, |X|/|Y| for normals, the Cayley transform of a skew-symmetric matrix, MLE on a restricted parameter space).
- A generic skill ("find an MLE/UMVUE/MoM estimate", "Bayes' theorem", "compute a limit", "test a series", "change the order of integration") is **not** a concept repeat.
- Every `repeat_of` now points to the earliest matching root. Near-chains were collapsed (e.g. 2025-Q32 → 2023-Q27 → 2020-Q4 became → 2012-Q16.a).

| kind | before | after |
|---|---|---|
| exact | 0 | 0 |
| near | 118 | 297 |
| concept | 157 | 20 |
| null | 503 | 461 |
| **flagged total** | **275** | **317** |

What happened to the 275 existing claims: 106 kept as they were, 110 concept → near (the set-up was identical; the workers mislabelled the kind), 30 repointed to the earliest root, 1 downgraded near → concept (2019-Q21), 28 removed. Separately, **70 missed near-repeats were added**: 2023 (the worker made zero repeat claims) and 2012–2025 rows that sat in the same archetype as an earlier row.

**Read this before using the numbers:** the workers were too generous with *concept*. But once the kind is fixed, strict near-matching finds *more* repeats, not fewer. JAM really does reuse set-ups: given-critical-region error probabilities ×14, MGF→distribution ×12, joint-pdf region probability ×8, parametric linear systems ×7, WLLN limit of a sample mean ×7, and so on.

Per year after review (near/concept): 2013 1/1, 2014 8/2, 2015 17/0, 2016 25/0, 2017 26/4, 2018 26/4, 2019 31/3, 2020 35/3, 2021 29/2, 2022 22/1, 2023 25/0, 2024 30/0, 2025 22/0.

If you want a tighter definition (near only when the same distribution family or function type recurs), most near counts in clusters like error-probabilities, mgf-identify-distribution and joint-pdf-region-probability would drop to concept or null. That's your call. The fixes file implements the rule as written.

### Near-repeat clusters after review (root ← later rows; * = changed by this review)

| root | canonical archetype | n later | later rows |
|---|---|---|---|
| 2012Q15 | error-probabilities-given-critical-region | 15 | 2015Q18*, 2015Q3*, 2016Q20*, 2017Q21*, 2018Q30, 2018Q59*, 2019Q60, 2020Q50*, 2021Q45*, 2022Q30*, 2023Q58*, 2023Q59*, 2024Q30*, 2024Q60*, 2025Q45* |
| 2013Q25 | mgf-identify-distribution | 11 | 2014Q3*, 2016Q5*, 2017Q6*, 2018Q20*, 2018Q56*, 2020Q55*, 2021Q17*, 2022Q46*, 2022Q47*, 2023Q22*, 2024Q45* |
| 2012Q16.a | parametric-linear-system-consistency | 9 | 2013Q19*, 2014Q22, 2015Q58, 2016Q31, 2020Q4*, 2021Q28*, 2022Q15*, 2023Q27*, 2025Q32* |
| 2012Q18.a | classify-critical-point-two-variables | 8 | 2014Q16, 2016Q27, 2017Q25, 2019Q2*, 2020Q32*, 2022Q32*, 2023Q7*, 2024Q2* |
| 2015Q12 | joint-pdf-region-probability | 8 | 2016Q43, 2017Q15*, 2019Q25*, 2020Q24*, 2022Q44*, 2023Q17*, 2024Q37*, 2025Q48* |
| 2013Q13 | mp-test-power-simple-vs-simple | 7 | 2014Q11, 2017Q22, 2020Q40*, 2021Q27, 2023Q10*, 2025Q5*, 2025Q8* |
| 2013Q30 | mixed-cdf-jumps | 7 | 2014Q14, 2015Q55, 2016Q40, 2017Q36*, 2018Q6, 2019Q35, 2021Q22* |
| 2014Q1 | count-real-roots-of-equation | 7 | 2015Q26, 2015Q49, 2017Q52*, 2018Q12, 2021Q58*, 2023Q16*, 2025Q11* |
| 2014Q28 | wlln-limit-of-sample-mean | 7 | 2016Q9, 2017Q17*, 2018Q49*, 2020Q29*, 2022Q24*, 2023Q42*, 2024Q47* |
| 2012Q12 | clt-limit-of-probability | 6 | 2014Q18, 2015Q53, 2016Q55, 2018Q21, 2021Q12*, 2021Q5* |
| 2013Q5 | eigenvalues-of-matrix-function | 6 | 2016Q52*, 2020Q53*, 2020Q54, 2021Q42*, 2023Q35*, 2024Q33* |
| 2014Q17 | area-between-curves | 6 | 2015Q60, 2017Q48, 2018Q42, 2020Q3*, 2021Q57*, 2025Q52* |
| 2014Q36 | volume-by-multiple-integral | 6 | 2016Q4, 2017Q54*, 2019Q53*, 2020Q15*, 2023Q26*, 2025Q53* |
| 2012Q5 | two-variable-differentiability-at-origin | 5 | 2020Q14*, 2021Q11*, 2022Q12*, 2023Q36*, 2024Q13* |
| 2013Q7 | normal-sample-derived-distributions | 5 | 2016Q18, 2017Q16*, 2017Q46*, 2020Q26*, 2024Q26* |
| 2013Q9 | mp-test-cutoff-via-chi-square | 5 | 2016Q37*, 2020Q30*, 2021Q23*, 2024Q29*, 2025Q22* |
| 2015Q57 | arc-length-of-curve | 5 | 2016Q50, 2019Q15, 2020Q33*, 2021Q50*, 2022Q13* |
| 2017Q4 | recursive-sequence-convergence | 5 | 2018Q1, 2018Q33, 2021Q26*, 2023Q24*, 2025Q31* |
| 2012Q22.b | joint-pdf-covariance | 4 | 2017Q45*, 2018Q27, 2021Q52*, 2024Q23* |
| 2015Q28 | leibniz-rule-derivative-value | 4 | 2016Q29, 2017Q24*, 2019Q3*, 2022Q14* |
| 2015Q6 | mp-test-rejection-region-form | 4 | 2016Q17, 2018Q29*, 2019Q29*, 2019Q40* |
| 2016Q42 | markov-inequality-bound | 4 | 2017Q12, 2019Q46, 2020Q7*, 2022Q20* |
| 2016Q51 | change-order-of-integration | 4 | 2018Q54, 2019Q43, 2020Q43*, 2021Q43* |
| 2018Q9 | bayes-theorem-numeric | 4 | 2019Q55*, 2021Q9*, 2022Q18*, 2023Q49* |
| 2020Q37 | normal-sample-derived-distributions | 4 | 2022Q38*, 2023Q32*, 2024Q39*, 2025Q36* |
| 2012Q2 | volume-of-revolution | 3 | 2015Q47, 2016Q3, 2019Q16 |
| 2012Q22.a | pdf-constants-from-normalisation-and-mean | 3 | 2015Q17, 2019Q56*, 2022Q55* |
| 2013Q15 | ci-coverage-from-minimum | 3 | 2014Q38, 2018Q36*, 2019Q59* |
| 2013Q29 | marginal-and-conditional-expectation | 3 | 2017Q57*, 2018Q24*, 2020Q45* |
| 2014Q19 | normal-linear-combination-probability | 3 | 2017Q43*, 2020Q47*, 2023Q46* |
| 2015Q19 | total-variance-hierarchical | 3 | 2019Q57, 2020Q36*, 2024Q22* |
| 2015Q22 | log-uniform-to-chi-square | 3 | 2016Q8, 2017Q41*, 2023Q45* |
| 2015Q29 | rank-and-consistency-of-system | 3 | 2019Q17*, 2021Q31*, 2024Q16* |
| 2015Q31 | series-convergence-implications | 3 | 2018Q32*, 2019Q31*, 2021Q8* |
| 2015Q36 | sufficient-statistic-identification | 3 | 2017Q39*, 2019Q28*, 2025Q38* |
| 2015Q52 | piecewise-pdf-interval-probability | 3 | 2017Q5, 2017Q55*, 2018Q55* |
| 2015Q54 | regression-estimates-from-sums | 3 | 2018Q10*, 2020Q21, 2022Q59* |
| 2016Q15 | chi-square-two-df-probability | 3 | 2020Q22*, 2022Q48*, 2025Q9* |
| 2012Q11 | f-reciprocal-quantile | 2 | 2020Q48, 2023Q3* |
| 2012Q23.a | crlb-for-function-of-parameter | 2 | 2015Q11, 2021Q40 |
| 2012Q3 | change-order-of-integration | 2 | 2014Q21, 2017Q23 |
| 2012Q4 | limit-as-derivative-definition | 2 | 2018Q51*, 2023Q51* |
| 2013Q12 | joint-pdf-normalising-constant | 2 | 2016Q56*, 2017Q14* |
| 2013Q14 | bayes-mixture-of-lifetimes | 2 | 2016Q22, 2020Q57 |
| 2013Q16 | binomial-of-binomial-probability | 2 | 2015Q13, 2019Q47* |
| 2014Q2 | probability-of-transformed-variable | 2 | 2016Q58, 2016Q59 |
| 2014Q25 | continuity-oscillating-function | 2 | 2016Q25, 2024Q12* |
| 2014Q40 | hierarchical-mixture-marginal | 2 | 2023Q29*, 2025Q19* |
| 2015Q20 | poisson-approximation-binomial | 2 | 2019Q23*, 2025Q29* |
| 2015Q24 | cayley-hamilton-matrix-equation | 2 | 2016Q30, 2018Q4 |
| 2015Q39 | limit-theorem-statements-sample-moments | 2 | 2020Q38*, 2024Q38* |
| 2015Q41 | min-order-statistic-expectation | 2 | 2024Q49*, 2025Q47* |
| 2015Q51 | marginal-and-conditional-expectation | 2 | 2019Q48*, 2022Q7* |
| 2016Q36 | mle-uniform-location-nonunique | 2 | 2020Q27, 2021Q19 |
| 2016Q39 | chi-square-pivot-confidence-interval | 2 | 2017Q20*, 2020Q28* |
| 2016Q53 | polar-coordinates-double-integral | 2 | 2020Q16*, 2024Q52* |
| 2016Q54 | series-sum-evaluation | 2 | 2017Q50, 2019Q11 |
| 2017Q13 | sum-of-geometrics-negative-binomial | 2 | 2018Q57, 2020Q23 |
| 2017Q7 | pmf-from-constraints | 2 | 2019Q6*, 2024Q55* |
| 2018Q48 | inclusion-exclusion-at-least-k-events | 2 | 2021Q25*, 2023Q8* |
| 2019Q41 | riemann-sum-limit | 2 | 2021Q1*, 2022Q11* |
| 2019Q44 | orthogonal-matrix-entries | 2 | 2020Q34*, 2024Q53* |
| 2019Q50 | t-confidence-interval | 2 | 2023Q33*, 2024Q59* |
| 2022Q56 | multinomial-moments | 2 | 2023Q34*, 2025Q34* |
| 2022Q60 | p-value-computation | 2 | 2023Q28*, 2024Q10* |
| 2012Q10 | correlation-of-partial-sums | 1 | 2015Q2 |
| 2012Q19.a | evaluate-multiple-integral | 1 | 2021Q44* |
| 2012Q19.b | inverse-via-cayley-hamilton | 1 | 2019Q18 |
| 2012Q25.b | sample-size-from-alpha-beta | 1 | 2019Q30* |
| 2012Q8 | geometric-memoryless | 1 | 2015Q42 |
| 2012Q9 | parameter-from-pmf-relation | 1 | 2019Q7* |
| 2013Q1 | conditional-probability-set-algebra | 1 | 2015Q5 |
| 2013Q11 | inverse-moment-of-gamma | 1 | 2019Q58* |
| 2013Q18 | limit-of-sequence-expression | 1 | 2016Q48 |
| 2013Q6 | clt-limit-of-probability | 1 | 2020Q9* |
| 2014Q29 | umvue-identify-formula | 1 | 2018Q39* |
| 2014Q4 | parallel-system-reliability | 1 | 2015Q45 |
| 2014Q6 | identify-linear-transformation | 1 | 2015Q7 |
| 2014Q9 | series-convergence-parameter-range | 1 | 2017Q26* |
| 2015Q16 | consistency-of-estimators | 1 | 2016Q21 |
| 2015Q25 | matrix-rank-statements | 1 | 2025Q13* |
| 2015Q43 | mle-restricted-parameter-space | 1 | 2021Q46* |
| 2015Q9 | function-injective-surjective-check | 1 | 2021Q2 |
| 2016Q1 | rank-of-given-matrix | 1 | 2020Q44 |
| 2016Q19 | umvue-identify-formula | 1 | 2021Q18* |
| 2016Q24 | series-convergence-pair | 1 | 2024Q11* |
| 2016Q26 | mvt-consequences-from-values | 1 | 2024Q32* |
| 2016Q41 | normal-sample-derived-distributions | 1 | 2024Q9* |
| 2016Q45 | normal-approximation-binomial-limit | 1 | 2024Q25* |
| 2017Q19 | method-of-moments-numeric | 1 | 2018Q28 |
| 2017Q27 | limit-via-series-expansion | 1 | 2020Q13* |
| 2017Q34 | mvt-consequences-from-values | 1 | 2020Q51* |
| 2017Q44 | joint-pmf-conditional-probability | 1 | 2018Q25 |
| 2017Q60 | gamma-parameters-from-moments | 1 | 2018Q5 |
| 2018Q18 | skew-symmetric-matrix-properties | 1 | 2019Q34* |
| 2018Q35 | pairwise-vs-mutual-independence | 1 | 2024Q18* |
| 2018Q37 | consistency-of-estimators | 1 | 2019Q39 |
| 2018Q45 | conditional-probability-counting | 1 | 2019Q45 |
| 2019Q4 | linear-map-from-basis-images | 1 | 2020Q17 |
| 2020Q19 | sampling-without-replacement-count | 1 | 2024Q4* |
| 2020Q31 | limsup-liminf-of-sequence | 1 | 2022Q41* |
| 2020Q46 | total-probability-over-discrete-rv | 1 | 2021Q15* |
| 2020Q5 | probability-bounds-intersection-union | 1 | 2021Q30 |
| 2020Q6 | expectation-of-function-discrete | 1 | 2022Q6 |
| 2021Q14 | cauchy-ratio-of-normals | 1 | 2023Q37* |
| 2021Q34 | lagrange-extrema-on-circle | 1 | 2022Q51* |
| 2021Q48 | mixture-distribution-variance | 1 | 2024Q19* |
| 2021Q51 | double-integral-change-of-variables | 1 | 2022Q52* |
| 2022Q19 | waiting-time-pattern-expectation | 1 | 2025Q55* |
| 2022Q57 | scaled-min-uniform-limit | 1 | 2024Q8* |
| 2023Q30 | nearest-point-on-surface | 1 | 2025Q51 |
| 2023Q44 | constant-for-unbiased-estimator | 1 | 2025Q21* |
| 2024Q41 | radius-of-convergence | 1 | 2025Q42 |

### Concept repeats kept (20)

| row | repeat_of | archetype |
|---|---|---|
| 2013Q8 | 2012Q23.b | unbiased-consistent-check-of-estimator |
| 2014Q10 | 2013Q9 | mp-test-cutoff-single-observation |
| 2014Q34 | 2013Q27 | mme-mle-uniform-scale-family |
| 2017Q10 | 2012Q23.b | compare-estimators-unbiased-consistent-efficient |
| 2017Q33 | 2013Q17 | rational-irrational-piecewise-continuity |
| 2017Q35 | 2016Q35 | conditional-probability-inequalities |
| 2017Q56 | 2015Q41 | min-order-statistic-probability |
| 2018Q11 | 2016Q34 | greatest-integer-discontinuity-points |
| 2018Q34* | 2014Q25 | oscillating-function-extremum-differentiability |
| 2018Q37 | 2014Q34 | consistency-of-estimators |
| 2018Q50 | 2015Q43 | mle-discrete-parameter-space |
| 2019Q10 | 2014Q41 | lrt-rejection-region-form |
| 2019Q21* | 2015Q22 | transformation-to-chi-square |
| 2019Q4 | 2014Q7 | linear-map-on-basis-coordinates |
| 2020Q18 | 2019Q34 | cayley-transform-skew-symmetric |
| 2020Q2 | 2013Q17 | piecewise-differentiability-constants |
| 2020Q58* | 2012Q24.b | umvue-numeric-estimate |
| 2021Q16 | 2020Q56 | integer-fractional-part-of-rv |
| 2021Q54* | 2015Q20 | poisson-approximation-binomial |
| 2022Q33 | 2018Q18 | orthogonal-skew-matrix-statements |

### Claims removed (→ null)

| row | was | archetype |
|---|---|---|
| 2015Q37 | concept:2012Q23.b | unbiased-consistent-check-of-estimator |
| 2016Q13 | concept:2012Q23.b | unbiased-consistent-check-of-estimator |
| 2016Q32 | concept:2014Q24 | sequence-and-its-series-convergence |
| 2016Q51 | concept:2012Q3 | change-order-of-integration |
| 2017Q30 | concept:2015Q57 | arc-length-of-curve |
| 2017Q34 | concept:2016Q26 | mvt-consequences-from-values |
| 2017Q38 | concept:2012Q23.a | crlb-attainable-variance-check |
| 2017Q53 | concept:2015Q57 | arc-length-of-curve |
| 2018Q13 | concept:2013Q24 | extrema-on-closed-region |
| 2018Q47 | concept:2013Q1 | conditional-probability-set-algebra |
| 2018Q9 | concept:2013Q14 | bayes-theorem-numeric |
| 2019Q13 | concept:2014Q1 | count-real-roots-of-equation |
| 2019Q19 | concept:2013Q1 | conditional-probability-set-algebra |
| 2019Q38 | concept:2013Q6 | clt-which-normalisation-converges |
| 2019Q49 | concept:2017Q19 | method-of-moments-numeric |
| 2019Q52 | concept:2018Q11 | floor-fractional-part-limit |
| 2019Q8 | concept:2014Q28 | wlln-limit-of-sample-mean |
| 2020Q10 | concept:2013Q8 | unbiased-consistent-check-of-estimator |
| 2020Q41 | concept:2013Q18 | limit-of-sequence-expression |
| 2022Q17 | concept:2012Q7 | classical-counting-probability |
| 2022Q49 | concept:2017Q19 | method-of-moments-numeric |
| 2022Q53 | concept:2012Q1 | identify-eigenvector-of-given-matrix |
| 2024Q50 | concept:2023Q55 | umvue-numeric-estimate |
| 2024Q51 | concept:2023Q43 | limit-via-series-expansion |
| 2024Q54 | concept:2023Q49 | bayes-theorem-numeric |
| 2025Q43 | concept:2024Q51 | limit-via-series-expansion |
| 2025Q57 | concept:2023Q55 | umvue-numeric-estimate |
| 2025Q6 | concept:2024Q7 | expectation-of-function-discrete |

## 3. Topic consistency

The same structure was filed under different topics in different years. Proposals (in `topics` of the fixes file, 17 rows):

| uid | current | proposed | why |
|---|---|---|---|
| 2015-MS-Q20, 2019-MS-Q23, 2025-MS-Q29, 2021-MS-Q54 | Limit Theorems / Central limit theorem | Univariate Distributions / Standard discrete distributions | Poisson approximation to the binomial is not the CLT. The syllabus puts "limiting (approximation) cases" under the standard distributions |
| 2017-MS-Q9 | Limit Theorems / Modes of convergence | Univariate Distributions / CDF, PMF and PDF | P(mean = 2) is 0 for every n, since the mean is continuous. No limit theorem is needed |
| 2023-MS-Q5 | Limit Theorems / Laws of large numbers | Limit Theorems / Modes of convergence | (X1+X2+Xn)/4 doesn't average, so it's convergence in distribution, not the LLN |
| 2018-MS-Q12 | Diff. Calc. One Var. / Maxima and minima | … / Rolle's and mean value theorems | root counting, like the other 6 count-real-roots rows |
| 2014-MS-Q39 | Multivariate / Functions of random vectors | Univariate / Standard continuous distributions | linear combination of independent normals, like 2017-Q43, 2020-Q47, 2023-Q46 |
| 2019-MS-Q25 | Multivariate / Functions of random vectors | Multivariate / Joint, marginal and conditional distributions | region probability, like the other 9 joint-pdf-region rows |
| 2012-MS-Q5 | Diff. Calc. Two Var. / Limits and continuity (two variables) | … / Partial and total differentiation | asks about partials too. The other 5 rows of this archetype are filed here |
| 2017-MS-Q35 | Probability / Axioms and properties | Probability / Conditional probability and Bayes' theorem | the same archetype as 2016-Q35 and 2022-Q4 |
| 2019-MS-Q17 | Matrices / Rank, inverse and adjoint | Matrices / Systems of linear equations | solvability of Px=b, like 2015-Q29, 2021-Q31, 2024-Q16 |
| 2020-MS-Q6, 2022-MS-Q6 | Univariate / Standard discrete distributions | Univariate / Expectation, moments and quantiles | E(g(X)), like the other 4 rows of expectation-of-function-discrete |
| 2017-MS-Q54, 2019-MS-Q53 | Integral Calculus / Double integrals and change of order | Integral Calculus / Areas, volumes and arc lengths | volume of a solid, like the other 5 volume-by-multiple-integral rows |
| 2021-MS-Q14 | Sampling Distributions / F distribution | Multivariate / Functions of random vectors | moments of \|X\|/\|Y\|, the same variable as 2018-Q26 |

Looked at and left alone: log-uniform-to-chi-square (Chi-square vs Functions of a r.v. follows what each question asks), limit-via-series-expansion (L'Hospital vs Taylor are both defensible), inverse-moment-of-gamma (2013 gamma vs 2019 chi-square).

## 4. Low/medium-confidence items: blind second opinion

n = 82 (81 medium, 1 low). I assigned topic/subtopic from the summary before looking at the label.

| field | agree | n | rate |
|---|---|---|---|
| topic | 79 | 82 | 96% |
| subtopic | 78 | 82 | 95% |

Disagreements (all four are also in the `topics` fixes):

| uid | field | current | proposed | reason |
|---|---|---|---|---|
| 2015-MS-Q20 | topic | Limit Theorems / CLT | Univariate / Standard discrete distributions | Poisson approximation |
| 2025-MS-Q29 | topic | Limit Theorems / CLT | Univariate / Standard discrete distributions | Poisson approximation |
| 2017-MS-Q9 | topic | Limit Theorems / Modes of convergence | Univariate / CDF, PMF and PDF | continuous point probability |
| 2023-MS-Q5 | subtopic | Laws of large numbers | Modes of convergence | not an average |

The one low-confidence item (2015-Q34, even/odd parts of f) has no better home in the taxonomy. I agree with Limits and continuity.

Not checked: cognitive_type, and the page images. Everything was judged from the one-line summaries, so thin summaries (e.g. 2023-Q5 "as printed") deserve a look at the image.

