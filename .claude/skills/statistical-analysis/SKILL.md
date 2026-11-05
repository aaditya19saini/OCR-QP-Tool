---
name: statistical-analysis
description: Compute topic frequency, marks weightage, year-wise patterns, archetypes, repeats and priority tiers from validated JAM MS data. Use for any calculation, trend or prioritisation work.
---

# Statistical analysis

Prerequisite: `pyq.validate` exits 0 and the user has approved stage 3.

## Build
1. Write `pyq/master.py`. It joins extracted and classified data on `uid` into `outputs/master.csv` (sorted by year, uid), with `is_top_level` and `era` columns. All stats read this file and nothing else.
2. Write `pyq/stats.py`: deterministic pandas functions returning DataFrames. Each one gets a test on a tiny hand-computed fixture. The tests are the audit: there's no separate auditor.

## Eras
- **2012 is a different exam** (subjective, 300 marks). Report it as a separate old-format note, and never pool it into weightage or trends.
- Check 2014–2017 the same way from `papers.yaml` (totals, sections). Any paper whose format differs from 2018+ goes with the old-era note.
- The **main analysis is the current-format papers only**. State which years these are, and n.

## Definitions (use exactly)
| Metric | Formula |
|---|---|
| Question frequency | Count of top-level questions with that primary topic. Subparts never inflate totals. |
| % of questions | Count ÷ total top-level questions in the same scope |
| Marks weightage | Sum of `marks` over top-level questions. Report how many rows had null marks. |
| % of marks | Mean over papers of (topic marks ÷ that paper's `total_marks`) |
| Appearance rate | Papers where the topic appears ÷ papers in scope. The denominator is never the year span. |
| Recent | Same metrics over the last 3 available papers. State which. |

Frequency, weightage and consistency stay separate columns; they answer different questions.

## Trends
- **No significance tests.** With this few papers they'd be noise. Use the year-by-topic table and plain description: "appeared in 6 of 7 papers", "absent in the last 3 after 4 earlier appearances".
- Missing years are NaN, never 0.
- Never say a topic is "due".

## Repeats and archetypes
- These come straight from classification (`repeat_kind`, `archetype`). Count archetypes per topic and rank them by number of papers they appear in, citing uids as examples.

## Priority tiers
- Tiers apply at **subtopic** level (topics all appear in ~every paper, so topic tiers don't discriminate; topics are just ranked by marks share). One explicit rule in `pyq/stats.py`, quoted in the report: Tier 1 = appearance ≥ 0.8 **or** mean marks share ≥ 2%; Tier 3 = appearance < 0.4 **and** share < 1%; Tier 2 = else (thresholds ≈ subtopic quartiles 2015–2025).
- Any manual override needs a one-line reason.
- No tier means "skip". Foundational topics get flagged even if they're rare.

Stop and report the key tables for user approval before interpretation.
