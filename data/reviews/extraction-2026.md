# Extraction review: 2026 (MS2026.pdf)

Reviewer: extraction-verifier. This is a text paper (47 pages, "JAM 2026 / IIT BOMBAY" watermark), so it gets a 5-page image sample per the pdf-extraction skill: `random.Random(2026).sample(range(2,48),5)` → **PDF pages 8, 9, 22, 34, 43**. Truth: `data/pages/2026/pNNN.png`. The text layer was used only as a hint.

## Verdict

**PASS**: 0 critical, 0 minor on the sampled pages. The whole-file structural checks also pass.

## Checks

- **Whole file:** 60 records, uids Q1–Q60 contiguous, no duplicates and no subparts (`parent_uid` null everywhere). Marks: Q1–10 ×1 + Q11–30 ×2 + Q31–40 ×2 + Q41–50 ×1 + Q51–60 ×2 = 10+40+20+10+20 = **100**. Sections: A = Q1–30 MCQ, B = Q31–40 MSQ, C = Q41–60 NAT. All consistent.
- **Section headers** (text layer, consistent with the caller's spec): p2 "Section A: Q.1 – Q.10 Carry ONE mark each", p10 "Section A: Q.11 – Q.30 Carry TWO marks each", p30 "Section B: Q.31 – Q.40 Carry TWO marks each", p40 "Section C: Q.41 – Q.50 Carry ONE mark each", p44 "Section C: Q.51 – Q.60 Carry TWO marks each". None of the sampled pages carries a header, so these were not checked against images.
- **papers.yaml:** 100 marks / 60 Q, labelled INFERRED (p1 is a notation page with no totals; I confirmed this from the p001 text layer). The inference matches the header sum above.
- **Sampled pages (image-checked):**

| page | question on image | record pages | section/format/marks | summary |
|---|---|---|---|---|
| 8 | Q.9 only: 2-state DTMC diagram (1→1 0.25, 1→2 0.75, 2→1 0.5, 2→2 0.5); which (π₁,π₂) is the stationary distribution; options (A)–(D) | [8] ✓ | A / MCQ / 1 ✓ | ✓ diagram values correct, answer not given |
| 9 | Q.10 only: X₁..X₉, Y iid N(μ,σ²), X̄ and S² (divisor 8); distribution of (3/√10)(X̄−Y)/S; options χ²₈, χ²₉, t₈, t₉ | [9] ✓ | A / MCQ / 1 ✓ | ✓ |
| 22 | Q.23 only (the top row is blank, so Q22 does not spill over): independent X_n, P(X_n=n)=1/n²=1−P(X_n=0); P = mean-square convergence to 0, Q = convergence in probability to 0 | [22] ✓ | A / MCQ / 2 ✓ | ✓ |
| 34 | Q.35 only: f_X = 1/2 on (0,1), 1/4 on (1,3); Y=X², Z=1/X; options: pdf of Y, pdf of Z, E(Y)<∞ and E(Z)<∞, Y positively skewed; "is/are true" | [34] ✓ | B / MSQ / 2 ✓ | ✓ |
| 43 | Q.50 only: X₁,X₂,X₃ sample from U(1,2); P(X₍₃₎ > 1.5), rounded to 2 decimals | [43] ✓ | C / NAT / 1 ✓ | ✓ |

## Findings

| uid | field | recorded | image shows | page | severity |
|---|---|---|---|---|---|
| none | | | | | |

## Flags resolved / confirmed

- **Q9 `figure-read-from-image`: confirmed** (p8). The transition probabilities in the summary match the diagram.
- **`checked-image` on Q9, Q10, Q23, Q35, Q50: confirmed.**
- There are no low- or medium-confidence records.

## Notes

- Only 5 of 46 question pages were image-checked. The other 55 summaries and their page numbers were not verified here.
- The section headers and the "no totals on p1" observation come from the text layer, not the images.
