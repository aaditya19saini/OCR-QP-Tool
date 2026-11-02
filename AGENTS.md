# AGENTS.md

Instructions for any coding agent (Codex, Claude Code, others) working in this repo.

**`CLAUDE.md` is the single source of truth.** Read it fully before doing anything. It holds the project rules, data-integrity rules, directory contract, record schema, commands, per-paper quirks, lessons learned, and the **current state and resume plan**. This file is a short summary; if it ever disagrees with CLAUDE.md, CLAUDE.md wins.

## What this is
A verified question-level dataset and statistics report for IIT JAM Mathematical Statistics (MS) papers 2012–2025. Spec: `docs/guide.md`, narrowed by the "Scope decisions" in CLAUDE.md.

## Status (2026-11-02)
- Done: all 14 papers OCR'd and audited, all 14 extracted and classified (778 rows, validator 0 errors), analysis code tested.
- Paused 2026-11-02 after Stage 3 (validation complete: 778 rows, 0 errors, classification reviewed). Next: user go-ahead, then the analysis plan (step 6 in CLAUDE.md, main scope 2015–2025) and the report.

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
