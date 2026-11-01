"""Join frozen extracted + classified records into outputs/master.csv (the only input for statistics).

Usage: python -m pyq.master
Adds: is_top_level, era ("current" = 60 questions / 100 marks per papers.yaml, else "old"), paper_total_marks.
"""
import json

import pandas as pd

from .common import CLASSIFIED, EXTRACTED, OUTPUTS, IntegrityError, load_yaml, read_jsonl, setup_logging, verify_manifest


def era(paper: dict) -> str:
    return "current" if paper.get("total_marks") == 100 and paper.get("expected_questions") == 60 else "old"


def build(extracted: list[dict], classified: list[dict], papers: dict) -> pd.DataFrame:
    cls = {r["uid"]: r for r in classified}
    if missing := [r["uid"] for r in extracted if r["uid"] not in cls]:
        raise IntegrityError(f"{len(missing)} extracted questions have no classification, e.g. {missing[:3]}")
    rows = []
    for r in extracted:
        c = cls[r["uid"]]
        p = papers[r["year"]]
        rows.append({
            **{k: r[k] for k in ("uid", "parent_uid", "year", "section", "format", "marks", "summary", "source_file", "confidence")},
            "pages": json.dumps(r["pages"]), "flags": json.dumps(r["flags"]),
            **{k: c[k] for k in ("subject", "topic", "subtopic", "cognitive_type", "archetype", "repeat_of", "repeat_kind", "taxonomy_version")},
            "class_confidence": c["confidence"],
            "secondary_concepts": json.dumps(c["secondary_concepts"]),
            "is_top_level": r["parent_uid"] is None,
            "era": era(p), "paper_total_marks": p.get("total_marks"),
        })
    df = pd.DataFrame(rows)
    df["qno"] = df["uid"].str.extract(r"Q(\d+)", expand=False).astype(int)
    return df.sort_values(["year", "qno", "uid"]).drop(columns="qno").reset_index(drop=True)


def main() -> None:
    log = setup_logging("master")
    verify_manifest()
    papers = load_yaml("papers.yaml")["papers"]
    ext, cls = [], []
    for f in sorted(EXTRACTED.glob("*.jsonl")):
        ext += read_jsonl(f)
        cf = CLASSIFIED / f.name
        if not cf.exists():
            raise IntegrityError(f"{f.stem}: extracted but not classified")
        cls += read_jsonl(cf)
    df = build(ext, cls, papers)
    df.to_csv(OUTPUTS / "master.csv", index=False)
    log.info("master.csv: %d rows, %d top-level, years %s", len(df), int(df.is_top_level.sum()), sorted(df.year.unique()))


if __name__ == "__main__":
    main()
