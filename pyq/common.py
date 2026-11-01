"""Shared paths, config loading, logging and the raw-data integrity check."""
import hashlib
import json
import logging
import platform
import subprocess
import sys
from datetime import datetime
from importlib import metadata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
MANIFEST = RAW / "MANIFEST.sha256"
PAGES = ROOT / "data" / "pages"
EXTRACTED = ROOT / "data" / "extracted"
CLASSIFIED = ROOT / "data" / "classified"
OUTPUTS = ROOT / "outputs"
LOGS = ROOT / "logs"
CONFIG = ROOT / "config"


class IntegrityError(Exception):
    """Raw data or a frozen dataset does not match what it should be. Stop the run."""


def load_yaml(name: str) -> dict:
    return yaml.safe_load((CONFIG / name).read_text()) or {}


def read_jsonl(path: Path) -> list[dict]:
    out = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise IntegrityError(f"{path.name}:{n} is not valid JSON: {e}") from e
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_manifest() -> None:
    """Every raw PDF must match its recorded hash, and no PDF may be unlisted."""
    if not MANIFEST.exists():
        raise IntegrityError("data/raw/MANIFEST.sha256 missing; run `python -m pyq.inventory` first")
    listed = {}
    for line in MANIFEST.read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        listed[name] = digest
    on_disk = {p.name for p in RAW.glob("*.pdf")}
    if on_disk != set(listed):
        raise IntegrityError(f"raw files differ from manifest: added={on_disk - set(listed)} missing={set(listed) - on_disk}")
    bad = [n for n, d in listed.items() if sha256(RAW / n) != d]
    if bad:
        raise IntegrityError(f"raw PDFs changed since manifest was written: {bad}")


def setup_logging(stage: str) -> logging.Logger:
    """Console + logs/<stage>-<timestamp>.log, starting with a header that pins the run's inputs."""
    LOGS.mkdir(exist_ok=True)
    logfile = LOGS / f"{stage}-{datetime.now():%Y%m%d-%H%M%S}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stderr), logging.FileHandler(logfile)],
        force=True,
    )
    log = logging.getLogger(stage)
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        sha += "+dirty" if dirty else ""
    except (subprocess.CalledProcessError, FileNotFoundError):
        sha = "no-commit"
    pkgs = {p: metadata.version(p) for p in ("pymupdf", "pandas", "numpy", "pyyaml")}
    log.info("run header %s", json.dumps({
        "stage": stage,
        "git": sha,
        "manifest": sha256(MANIFEST) if MANIFEST.exists() else None,
        "python": platform.python_version(),
        "packages": pkgs,
    }))
    return log
