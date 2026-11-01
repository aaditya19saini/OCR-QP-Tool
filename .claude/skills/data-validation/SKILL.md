---
name: data-validation
description: Validate the JAM MS question datasets (completeness, marks totals, schema, taxonomy, traceability) and write the extraction/classification audit. Use before any analysis, after any data edit, or when asked to check data quality.
---

# Data validation

## Steps
1. `.venv/bin/python -m pyq.validate` (all years). Exit code 1 means stop: fix the data, never relax the check.
   - It checks: the manifest, required fields, enum values, unique uids, parent links, question count vs `expected_questions`, top-level marks sum vs `total_marks`, subpart sums vs parent, taxonomy membership and version, and repeat-field consistency.
   - Tests in `tests/test_validate.py` prove these checks fire. Add a test for any new check.
2. Cross-paper checks the script can't do (do these by reading the data):
   - Numbering gaps: Q1..Qn contiguous per year.
   - Years with null totals: are they truly unprinted? Check the instructions page.
   - Consistent topic usage across years (e.g. the same concept split across two topics).
3. Write `outputs/audit.csv` (this feeds the report's limitations section) with columns `uid, year, issue_type, detail, status`. Issue types: missing, unreadable, ambiguous, marks-null, low-confidence-extraction, low-confidence-classification, reviewer-disagreement. The status is open or resolved with the resolution.
4. Summarise for the user: errors (must be 0), open issues by type, and which years are analysis-ready.

## Rules
- Missing ≠ zero: a null field or missing year is reported as missing.
- Don't "fix" by guessing. Unresolvable items stay flagged and go in the report's limitations.
- If you add a new automatic check, put it in `pyq/validate.py` with a test in `tests/test_validate.py`.
