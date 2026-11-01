---
name: report-generation
description: Produce the deliverables (one master CSV + one report with figures, printed to PDF) from approved JAM MS statistics. Use for any chart or report output.
---

# Report generation

There are two deliverables: **`outputs/master.csv`** (already built in stats) and **`outputs/report/jam_ms_report.pdf`**. No Excel workbook and no separate methodology doc: methodology and limitations are sections of the report.

## Figures (`pyq/report.py` → `outputs/figures/NN-name.png`, 200 dpi, matplotlib/seaborn)
Only figures that answer a guide §16 question:
1. marks share by topic (bar, sorted, with a cumulative line = Pareto)
2. year × topic heatmap of marks share
3. appearance rate by topic
4. question-format mix per year (stacked)
5. top archetypes by number of papers

Every figure must have:
- a descriptive title
- labelled axes with units
- the period covered
- the footer `Source: JAM MS papers <years>; n = <questions> questions, <papers> papers`

Year axes show missing years as labelled gaps (grey "no paper"), never zeros. Use one colorblind-safe palette.

## Report (`pyq/report.py` → `outputs/report/jam_ms_report.html` → PDF)
- Sections: summary, overview, topic frequency & weightage, year-wise patterns, archetypes & repeats, priority tiers, future areas, preparation advice, old-format note (2012 etc.), methodology & limitations.
- Every number is pulled from the computed tables, never typed by hand.
- Future areas are **hypotheses** with an evidence strength (strong / moderate / weak).
- Study-time allocation is proportional to the evidence, with the "don't skip syllabus topics" caveat.
- Limitations include the open items from `outputs/audit.csv`.
- Plain HTML with inline CSS and figures embedded as files next to it.
- PDF: `brave --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=outputs/report/jam_ms_report.pdf outputs/report/jam_ms_report.html`

## Finish
Run it twice and diff `master.csv` and the tables: they must be identical. Stop for user review.
