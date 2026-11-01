import pytest

from pyq import common
from pyq.validate import check_classified, check_extracted

PAPER = {"file": "MS2099.pdf", "total_marks": 3, "expected_questions": 2}
TAX = {"version": "t1", "subjects": {"Statistics": {"Estimation": ["MLE"]}}}


def q(uid, marks=1, parent=None, **kw):
    r = {"uid": uid, "parent_uid": parent, "year": 2099, "section": "A", "format": "MCQ",
         "marks": marks, "summary": "MLE of mu for N(mu,1) sample", "source_file": "MS2099.pdf",
         "pages": [3], "confidence": "high", "flags": []}
    return r | kw


def c(uid, **kw):
    r = {"uid": uid, "subject": "Statistics", "topic": "Estimation", "subtopic": "MLE",
         "secondary_concepts": [], "cognitive_type": "numerical",
         "archetype": "mle-of-param", "repeat_of": None, "repeat_kind": None,
         "confidence": "high", "rationale": "x", "taxonomy_version": "t1"}
    return r | kw


def test_clean_paper_passes():
    recs = [q("A-Q1"), q("A-Q2", marks=2), q("A-Q2.a", 1, "A-Q2"), q("A-Q2.b", 1, "A-Q2")]
    errors, _ = check_extracted(recs, 2099, PAPER)
    assert errors == []
    assert check_classified([c("A-Q1")], {"A-Q1", "A-Q2"}, TAX)[0] == []


@pytest.mark.parametrize("recs, needle", [
    ([q("A-Q1"), q("A-Q1", marks=2)], "duplicate"),
    ([q("A-Q1"), q("A-Q2")], "marks sum 2 != paper total 3"),
    ([q("A-Q1", marks=3)], "1 top-level questions"),
    ([q("A-Q1"), q("A-Q2", marks=2), q("A-Q2.a", 1, "A-Q2")], "subpart marks 1 != parent 2"),
    ([q("A-Q1"), q("A-Q2", marks=2, format="essay")], "bad format"),
    ([q("A-Q1"), q("A-Q2", marks=2, pages=[])], "no page reference"),
    ([q("A-Q1"), q("A-Q2", marks=2, parent="A-Q9")], "not in file"),
])
def test_extraction_errors_caught(recs, needle):
    errors, _ = check_extracted(recs, 2099, PAPER)
    assert any(needle in e for e in errors), errors


def test_null_marks_never_fail_or_get_guessed():
    errors, warnings = check_extracted([q("A-Q1", marks=None), q("A-Q2", marks=2)], 2099, PAPER)
    assert errors == []
    assert any("not checkable" in w for w in warnings)


@pytest.mark.parametrize("rec, needle", [
    (c("A-Q1", topic="Regression"), "not under Statistics"),
    (c("A-Q1", subtopic="UMVUE"), "subtopic"),
    (c("A-Q1", taxonomy_version="t0"), "taxonomy_version"),
    (c("A-Q1", repeat_kind="near"), "inconsistent"),
    (c("A-Q7"), "not in extracted"),
])
def test_classification_errors_caught(rec, needle):
    errors, _ = check_classified([rec], {"A-Q1"}, TAX)
    assert any(needle in e for e in errors), errors


def test_tampered_raw_pdf_raises(tmp_path, monkeypatch):
    pdf = tmp_path / "MS2099.pdf"
    pdf.write_bytes(b"original")
    manifest = tmp_path / "MANIFEST.sha256"
    manifest.write_text(f"{common.sha256(pdf)}  MS2099.pdf\n")
    monkeypatch.setattr(common, "RAW", tmp_path)
    monkeypatch.setattr(common, "MANIFEST", manifest)
    common.verify_manifest()
    pdf.write_bytes(b"tampered")
    with pytest.raises(common.IntegrityError, match="changed"):
        common.verify_manifest()
    (tmp_path / "MS2100.pdf").write_bytes(b"x")
    with pytest.raises(common.IntegrityError, match="added"):
        common.verify_manifest()
