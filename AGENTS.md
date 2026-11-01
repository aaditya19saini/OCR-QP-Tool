# AGENTS.md

Instructions for any coding agent (Codex, Claude Code, others) working in this repo.

**`CLAUDE.md` is the single source of truth.** Read it fully before doing anything. It holds the project rules, data-integrity rules, directory contract, record schema, commands, per-paper quirks, lessons learned, and the **current state and resume plan**. This file is a short summary; if it ever disagrees with CLAUDE.md, CLAUDE.md wins.

## What this is
A verified question-level dataset and statistics report for IIT JAM Mathematical Statistics (MS) papers 2012–2025. Spec: `docs/guide.md`, narrowed by the "Scope decisions" in CLAUDE.md.

## Status (2026-11-01)
- Done: all 14 papers OCR'd and audited, all 14 extracted (validator 0 errors), 5 years classified (2012, 2013, 2023, 2024, 2025), analysis code tested.
- Next: classify 2014–2022, enter printed totals in `config/papers.yaml`, image-verify scans 2014/2017/2025, add a pre-2026 Differential Equations topic, merge archetypes, then stats and report. Full checklist in CLAUDE.md, "Current state and resume plan".

## Hard rules (summary)
- Never fabricate or infer exam data. Unknown = `null` + flag.
- `data/raw/` is immutable. Every script verifies its SHA-256 manifest.
- Frozen data (`data/extracted`, `data/classified`, `data/ocr`) is changed only by reviewed edits, and every change is committed.
- Stop for the user's approval between stages.
- Before committing: `.venv/bin/python -m pytest -q` and `.venv/bin/python -m pyq.validate`.

## Setup
```
uv venv -p 3.12 .venv && uv pip install -p .venv -r requirements.txt
.venv/bin/python -m pytest -q
```
Local OCR needs `~/.cache/pyq-ocr/` (not in git). See CLAUDE.md, Commands.
