# OCR-QP-Tool — JAM MS question-paper analytics

Turns IIT JAM Mathematical Statistics question papers (2012–2025, official PDFs from
[jam2026.iitb.ac.in/oldQP.html](https://jam2026.iitb.ac.in/oldQP.html)) into a verified question-level
dataset, then topic/marks statistics and a preparation report.

- `data/raw/` official PDFs + SHA-256 manifest (immutable)
- `data/ocr/` local OCR text (PaddleOCR-VL 1.6 via llama.cpp, runs on a 4 GB GPU)
- `data/extracted/`, `data/classified/` frozen question records; `data/reviews/` verifier reports
- `pyq/` pipeline code; `CLAUDE.md` project rules; `docs/guide.md` spec

```
uv venv -p 3.12 .venv && uv pip install -p .venv -r requirements.txt
.venv/bin/python -m pytest -q
.venv/bin/python -m pyq.inventory && .venv/bin/python -m pyq.validate
```
