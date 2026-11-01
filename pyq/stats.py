"""Deterministic statistics over outputs/master.csv. Definitions follow .claude/skills/statistical-analysis/SKILL.md.

Main scope = top-level questions of current-format papers (60 Q / 100 marks). Old-format papers are reported separately.
"""
import pandas as pd

# Tier rule (quoted in the report): Tier 1 if appearance_rate >= 0.7 or mean marks share >= 8%;
# Tier 3 if appearance_rate < 0.3 and share < 3%; else Tier 2.
TIER1_RATE, TIER1_SHARE, TIER3_RATE, TIER3_SHARE = 0.7, 0.08, 0.3, 0.03
RECENT_PAPERS = 3


def scope(df: pd.DataFrame, era: str = "current") -> pd.DataFrame:
    return df[df.is_top_level & (df.era == era)]


def topic_table(df: pd.DataFrame, level: str = "topic") -> pd.DataFrame:
    """One row per subject/topic/subtopic over the given scope (pass an already-scoped frame)."""
    keys = {"subject": ["subject"], "topic": ["subject", "topic"], "subtopic": ["subject", "topic", "subtopic"]}[level]
    years = sorted(df.year.unique())
    recent = years[-RECENT_PAPERS:]
    totals = df.groupby("year").paper_total_marks.first()
    marks = df.groupby(keys + ["year"]).marks.sum(min_count=1).unstack("year").reindex(columns=years)
    share = marks.fillna(0).div(totals, axis=1)  # absent in a paper that exists = 0 share
    g = df.groupby(keys)
    out = pd.DataFrame({
        "questions": g.size(),
        "pct_questions": g.size() / len(df),
        "papers_appeared": g.year.nunique(),
        "appearance_rate": g.year.nunique() / len(years),
        "marks": g.marks.sum(min_count=1),
        "null_marks": g.marks.apply(lambda s: int(s.isna().sum())),
        "mean_marks_share": share.mean(axis=1),
        "avg_marks": g.marks.mean(),
        "max_marks": g.marks.max(),
        "min_marks": g.marks.min(),
        "recent_questions": df[df.year.isin(recent)].groupby(keys).size(),
        "n_archetypes": g.archetype.nunique(),
    })
    fmt = df.groupby(keys + ["format"]).size().unstack("format", fill_value=0).add_prefix("n_")
    out = out.join(fmt).fillna({"recent_questions": 0}).astype({"recent_questions": int})
    out.attrs.update(n_papers=len(years), n_questions=len(df), years=years, recent=recent)
    return out.sort_values(["mean_marks_share", "questions"], ascending=False)


def year_topic(df: pd.DataFrame, all_years: list[int], level: str = "topic", value: str = "share") -> pd.DataFrame:
    """Year x topic matrix. Years outside the scope stay NaN (missing, never 0)."""
    if value == "share":
        m = df.groupby(["year", level]).marks.sum().unstack(level).fillna(0)
        m = m.div(df.groupby("year").paper_total_marks.first(), axis=0)
    else:
        m = df.groupby(["year", level]).size().unstack(level).fillna(0)
    return m.reindex(all_years)


def format_mix(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.is_top_level].groupby(["year", "format"]).size().unstack("format", fill_value=0)


def archetypes(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["topic", "archetype"])
    return pd.DataFrame({
        "papers": g.year.nunique(), "questions": g.size(),
        "examples": g.uid.apply(lambda s: ", ".join(sorted(s)[:4])),
    }).sort_values(["papers", "questions"], ascending=False)


def tiers(tt: pd.DataFrame) -> pd.Series:
    def tier(r):
        if r.appearance_rate >= TIER1_RATE or r.mean_marks_share >= TIER1_SHARE:
            return 1
        if r.appearance_rate < TIER3_RATE and r.mean_marks_share < TIER3_SHARE:
            return 3
        return 2
    return tt.apply(tier, axis=1).rename("tier")
