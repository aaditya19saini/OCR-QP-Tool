---
name: question-classification
description: Classify extracted JAM MS questions by syllabus topic, cognitive type, archetype and repeat status into data/classified/<year>.jsonl. Use when tagging or re-tagging questions.
---

# Question classification

Prerequisites: `config/taxonomy.yaml` has a non-null `version` (built from the official syllabus in `docs/`), and the year's extraction is validated and approved.

## Rules
- `subject` / `topic` / `subtopic` must match `taxonomy.yaml` names **exactly**. If nothing fits, use the closest topic, confidence low, and explain in `rationale`. Never invent a topic. If the taxonomy itself looks wrong, raise it with the user (a taxonomy change bumps `version`, and every year gets re-validated).
- Each question gets one primary topic. Other concepts go in `secondary_concepts` (taxonomy names where possible).
- Classify subparts individually. The parent row gets the topic of the dominant part.
- `cognitive_type` takes one of: recall, conceptual, numerical, derivation, proof, application, data-interpretation, multi-concept, logical-reasoning.
- `archetype` is a short kebab-case label for the problem structure (e.g. `mle-of-uniform-endpoint`, `mgf-identify-distribution`). Reuse existing labels: list them first with `cat data/classified/*.jsonl` and check for near-synonyms. Same structure means the same label.
- Repeats are judged only against **earlier** years:
  - `exact`: same question.
  - `near`: same structure with changed numbers or assumptions.
  - `concept`: same specific concept through a different structure.
  - Same topic alone gets `null`, not `concept`.
  - Set `repeat_of` to the earliest matching uid.
- `confidence`: high / medium / low, honestly.
- `taxonomy_version`: copy it from `taxonomy.yaml`.

## Steps
1. Read `data/extracted/<year>.jsonl`, the taxonomy, and the archetypes already in use. If a summary is too thin to classify, open the page image it cites.
2. Write `data/classified/<year>.jsonl`, one line per extracted uid.
3. `.venv/bin/python -m pyq.validate <year>`. All errors must be fixed.
4. After all years are classified, launch the `classification-reviewer` agent on the low- and medium-confidence items and the repeat claims. Resolve its disagreements with the user.
5. Stop and report: topic counts, low-confidence count, new archetypes, repeat pairs.
