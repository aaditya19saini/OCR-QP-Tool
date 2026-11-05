import math

import pandas as pd
import pytest

from pyq.master import build, era
from pyq.common import IntegrityError
from pyq import stats

# Two current-format papers (totals 100) and one old paper; hand-computed expectations below.
ROWS = [
    # year, q, topic, marks, format, parent
    (2020, 1, "Estimation", 50, "MCQ", None),
    (2020, 2, "Probability", 50, "NAT", None),
    (2021, 1, "Estimation", 20, "MCQ", None),
    (2021, 2, "Estimation", 80, "MSQ", None),
    (2021, 3, "Probability", None, "NAT", "2021-MS-Q2"),  # subpart: never counted in top-level stats
    (2012, 1, "Probability", 300, "subjective", None),
]
PAPERS = {2020: {"total_marks": 100, "expected_questions": 60}, 2021: {"total_marks": 100, "expected_questions": 60},
          2012: {"total_marks": 300, "expected_questions": 25}}


def frame():
    ext, cls = [], []
    for y, q, topic, marks, fmt, parent in ROWS:
        uid = f"{y}-MS-Q{q}"
        ext.append({"uid": uid, "parent_uid": parent, "year": y, "section": "A", "format": fmt, "marks": marks,
                    "summary": "s", "source_file": f"MS{y}.pdf", "pages": [1], "confidence": "high", "flags": []})
        cls.append({"uid": uid, "subject": "Statistics", "topic": topic, "subtopic": None, "secondary_concepts": [],
                    "cognitive_type": "numerical", "archetype": f"{topic[:3]}-{q}", "repeat_of": None,
                    "repeat_kind": None, "confidence": "high", "taxonomy_version": "t"})
    return build(ext, cls, PAPERS)


def test_era_split_and_subparts_excluded():
    df = frame()
    assert era(PAPERS[2012]) == "old" and era(PAPERS[2020]) == "current"
    s = stats.scope(df)
    assert sorted(s.uid) == ["2020-MS-Q1", "2020-MS-Q2", "2021-MS-Q1", "2021-MS-Q2"]


def test_topic_table_hand_computed():
    tt = stats.topic_table(stats.scope(df := frame())).droplevel("subject")
    est, prob = tt.loc["Estimation"], tt.loc["Probability"]
    assert est.questions == 3 and prob.questions == 1
    assert est.pct_questions == pytest.approx(0.75)
    assert est.appearance_rate == 1.0 and prob.appearance_rate == 0.5
    # shares: Estimation 0.5 (2020), 1.0 (2021) -> mean 0.75; Probability 0.5, 0 -> mean 0.25 (absent in an existing paper = 0)
    assert est.mean_marks_share == pytest.approx(0.75) and prob.mean_marks_share == pytest.approx(0.25)
    assert est.max_marks == 80 and est.min_marks == 20


def test_year_topic_missing_years_are_nan():
    m = stats.year_topic(stats.scope(frame()), [2012, 2020, 2021])
    assert math.isnan(m.loc[2012, "Estimation"])  # old paper outside scope: missing, not 0
    assert m.loc[2021, "Probability"] == 0  # present paper, topic absent: 0


def test_tiers_rule():
    tt = pd.DataFrame({"appearance_rate": [0.8, 0.2, 0.5, 0.1], "mean_marks_share": [0.005, 0.005, 0.015, 0.03]})
    assert list(stats.tiers(tt)) == [1, 3, 2, 1]  # rare but heavy -> tier 1


def test_unclassified_question_raises():
    with pytest.raises(IntegrityError, match="no classification"):
        build([{"uid": "x"}], [], PAPERS)
