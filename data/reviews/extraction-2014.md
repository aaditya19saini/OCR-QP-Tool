# Extraction review — 2014 (MS2014.pdf)

Reviewer: extraction-verifier. Truth: page images `data/pages/2014/p001.png`–`p038.png`. Question pages are p003–p012 (Part I) and the even pages p014–p028 (Part II, one question per page, odd pages blank/rough work). p029–p038 are rough-work and examiner mark-sheet pages with no questions (p036 is the Part-II marks table listing Q36–Q43). OCR text used as a reading aid; the `checked-image` items were re-read on the image.

## Verdict

**PASS**: 0 critical, 1 minor.

## Printed totals (for config/papers.yaml)

- **p001 (cover / general instructions):** "Maximum Marks : 100", "Time : 3 Hours". Instruction 10: "Part-I consists of 35 objective type questions. The first 10 questions carry ONE mark each and the rest 25 questions carry TWO marks each." Instruction 11: four choices, only ONE correct. Instruction 14: "Part-II has 8 subjective type questions."
- **p003 (important note):** "Part-II consists of 8 descriptive type questions each carrying five marks." Header "Q. 1 – Q. 10 carry one mark each."
- **p006:** "Q. 11 – Q. 35 carry two marks each." **p014:** "Part-II: Descriptive Questions — Q. 36 – Q. 43 carry five marks each."
- Totals: 10×1 + 25×2 + 8×5 = **100 marks, 43 questions**. Suggested entry: `total_marks: 100`, `expected_questions: 43`, `sections: {Part-I: "Q1-35 MCQ (Q1-10 1 mark, Q11-35 2 marks)", Part-II: "Q36-43 subjective, 5 marks"}`, `source: "MS2014.pdf p1 instructions 10,14; p3 note; headers p3, p6, p14"`.

## Checks

- **Completeness:** Q.1–Q.43 each appear exactly once; 43 records, no gaps, no extras. No printed subparts (Q37 and Q40 each ask two things in one paragraph; no (a)/(b) labels).
- **Pages:** Q1–3 p3, Q4–6 p4, Q7–10 p5, Q11–13 p6, Q14–17 p7, Q18–21 p8, Q22–24 p9, Q25–27 p10, Q28–31 p11, Q32–35 p12, Q36 p14, Q37 p16, Q38 p18, Q39 p20, Q40 p22, Q41 p24, Q42 p26, Q43 p28. All 43 `pages` values match.
- **Section/format/marks:** Q1–35 `Part-I` MCQ (four options each), Q1–10 = 1, Q11–35 = 2; Q36–43 `Part-II` subjective, 5 each. All records match. Sum = 100.
- **Summaries:** all 43 checked. No wrong distribution, parameter, statistic or quantity. None states an answer.

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| 2014-MS-Q32 | summary | "X,Y iid Bin(3,1/3): probability that 2x2 matrix with entries X/sqrt2, Y/sqrt2 is orthogonal" | Matrix P = [[X/√2, Y/√2], [−1/√2, 1/√2]]; the fixed second row is what defines the question and is missing | 12 | minor |

## Flags resolved / confirmed

- **Q7 `checked-image`: confirmed.** Image p5 shows basis (1,0,0), (1,1,0), (1,1,1). The OCR text wrongly repeats (1,1,0); the record is right.
- **Q21 `checked-image`: confirmed.** ∫₀¹∫_{x²}^{2x} f dy dx, change of order; summary accurate.
- **Q25 `checked-image`: confirmed** (p10). f = x sin(1/x²) for x≠0, f(0) = lim log(1+aₙ)/sin(aₙ+π/2) with lim aₙ^{1/n} = 1/4; asks continuity/differentiability at 0.
- **Q26 `checked-image`: confirmed** (p10). lim_{x→1/2} ∫_{1/2}^x cos²πt dt / (e^{2x}/2 − e(x²+1/4)). The "(L'Hospital)" tag is a method label added by the extractor, not printed.
- **Q37, Q40 `unmarked-subparts`: confirmed.** Each asks two quantities without (a)/(b) labels; storing as one 5-mark row is right.
- No low/medium-confidence records.

## Notes

- Several summaries carry extractor-added method labels in parentheses (Q3 "(normal)", Q18 "(CLT)", Q26 "(L'Hospital)", Q28 "(WLLN)", Q33 "(Weibull)"). Checked ones are correct; none gives the answer.
- Q35 (homogeneous ODE), Q42 (Bernoulli ODE), Q23 (linear ODE) are differential-equations questions — relevant to the known taxonomy gap.
