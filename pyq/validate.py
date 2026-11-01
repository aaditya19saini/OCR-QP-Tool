"""Validate frozen datasets. Claude's JSONL output is a trust boundary: nothing downstream reads it unchecked.

Usage: python -m pyq.validate [year ...]   (default: every year with an extracted file)
Exit code 1 if any error. Warnings are printed but don't fail.
"""
import sys

from .common import CLASSIFIED, EXTRACTED, load_yaml, read_jsonl, setup_logging, verify_manifest

FORMATS = {"MCQ", "MSQ", "NAT", "subjective"}
CONFIDENCE = {"high", "medium", "low"}
COGNITIVE = {
    "recall", "conceptual", "numerical", "derivation", "proof", "application",
    "data-interpretation", "multi-concept", "logical-reasoning",
}
REPEAT_KINDS = {None, "exact", "near", "concept"}

EXTRACTED_FIELDS = {
    "uid", "parent_uid", "year", "section", "format", "marks", "summary",
    "source_file", "pages", "confidence", "flags",
}
CLASSIFIED_FIELDS = {
    "uid", "subject", "topic", "subtopic", "secondary_concepts", "cognitive_type",
    "archetype", "repeat_of", "repeat_kind", "confidence", "rationale",
    "taxonomy_version",
}


def check_extracted(recs: list[dict], year: int, paper: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    uids = [r.get("uid") for r in recs]
    dupes = {u for u in uids if uids.count(u) > 1}
    if dupes:
        errors.append(f"duplicate uids: {sorted(dupes)}")
    known = set(uids)
    for r in recs:
        u = r.get("uid", "?")
        if missing := EXTRACTED_FIELDS - r.keys():
            errors.append(f"{u}: missing fields {sorted(missing)}")
            continue
        if r["year"] != year:
            errors.append(f"{u}: year {r['year']} in {year} file")
        if r["format"] not in FORMATS:
            errors.append(f"{u}: bad format {r['format']!r}")
        if r["confidence"] not in CONFIDENCE:
            errors.append(f"{u}: bad confidence {r['confidence']!r}")
        if r["parent_uid"] is not None and r["parent_uid"] not in known:
            errors.append(f"{u}: parent {r['parent_uid']} not in file")
        if r["source_file"] != paper["file"]:
            errors.append(f"{u}: source_file {r['source_file']} != {paper['file']}")
        if not r["pages"]:
            errors.append(f"{u}: no page reference")
        if not r["summary"].strip():
            errors.append(f"{u}: empty summary")
        if r["marks"] is None:
            warnings.append(f"{u}: marks not printed (null)")
        if r["confidence"] == "low" or set(r["flags"]) - {"checked-image"}:  # checked-image is a note, not a problem
            warnings.append(f"{u}: needs manual check ({r['confidence']}, flags={r['flags']})")

    # Subparts carry their own marks; totals count each top-level question once.
    top = [r for r in recs if r.get("parent_uid") is None]
    if (n := paper.get("expected_questions")) is not None and len(top) != n:
        errors.append(f"{year}: {len(top)} top-level questions, paper states {n}")
    if (total := paper.get("total_marks")) is not None:
        if any(r.get("marks") is None for r in top):
            warnings.append(f"{year}: marks total not checkable, some marks null")
        elif (s := sum(r["marks"] for r in top)) != total:
            errors.append(f"{year}: marks sum {s} != paper total {total}")
    for p in top:
        kids = [r for r in recs if r.get("parent_uid") == p["uid"]]
        if kids and p.get("marks") is not None and all(k.get("marks") is not None for k in kids):
            if (s := sum(k["marks"] for k in kids)) != p["marks"]:
                errors.append(f"{p['uid']}: subpart marks {s} != parent {p['marks']}")
    return errors, warnings


def check_classified(recs: list[dict], extracted_uids: set[str], taxonomy: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    subjects = taxonomy.get("subjects") or {}
    seen = set()
    for r in recs:
        u = r.get("uid", "?")
        if missing := CLASSIFIED_FIELDS - r.keys():
            errors.append(f"{u}: missing fields {sorted(missing)}")
            continue
        if u in seen:
            errors.append(f"{u}: classified twice")
        seen.add(u)
        if u not in extracted_uids:
            errors.append(f"{u}: not in extracted data")
        if r["taxonomy_version"] != taxonomy.get("version"):
            errors.append(f"{u}: taxonomy_version {r['taxonomy_version']} != {taxonomy.get('version')}")
        topics = subjects.get(r["subject"])
        if topics is None:
            errors.append(f"{u}: subject {r['subject']!r} not in taxonomy")
        elif r["topic"] not in topics:
            errors.append(f"{u}: topic {r['topic']!r} not under {r['subject']}")
        elif r["subtopic"] is not None and r["subtopic"] not in (topics[r["topic"]] or []):
            errors.append(f"{u}: subtopic {r['subtopic']!r} not under {r['topic']}")
        if r["cognitive_type"] not in COGNITIVE:
            errors.append(f"{u}: bad cognitive_type {r['cognitive_type']!r}")
        if r["confidence"] not in CONFIDENCE:
            errors.append(f"{u}: bad confidence {r['confidence']!r}")
        if r["repeat_kind"] not in REPEAT_KINDS or (r["repeat_kind"] is None) != (r["repeat_of"] is None):
            errors.append(f"{u}: repeat_of/repeat_kind inconsistent")
        if r["confidence"] == "low":
            warnings.append(f"{u}: low-confidence classification")
    if unclassified := extracted_uids - seen:
        warnings.append(f"{len(unclassified)} extracted questions not classified yet")
    return errors, warnings


def main(years: list[int]) -> int:
    log = setup_logging("validate")
    verify_manifest()
    papers = load_yaml("papers.yaml")["papers"]
    taxonomy = load_yaml("taxonomy.yaml")
    years = years or sorted(int(p.stem) for p in EXTRACTED.glob("*.jsonl"))
    n_err = 0
    for y in years:
        ext = read_jsonl(EXTRACTED / f"{y}.jsonl")
        errors, warnings = check_extracted(ext, y, papers[y])
        cls_path = CLASSIFIED / f"{y}.jsonl"
        if cls_path.exists():
            e, w = check_classified(read_jsonl(cls_path), {r["uid"] for r in ext}, taxonomy)
            errors += e
            warnings += w
        for m in warnings:
            log.warning("%d %s", y, m)
        for m in errors:
            log.error("%d %s", y, m)
        log.info("%d: %d records, %d errors, %d warnings", y, len(ext), len(errors), len(warnings))
        n_err += len(errors)
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main([int(a) for a in sys.argv[1:]]))
