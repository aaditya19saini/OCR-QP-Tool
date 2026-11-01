from pathlib import Path

import pytest

from pyq.ocr import clean

PNG = Path("p001.png")


def test_normal_output_is_stripped():
    assert clean("  Q.1 text \n\n", "stop", PNG) == "Q.1 text\n"


def test_whitespace_loop_after_text_is_kept():
    # 2017 p2: model emitted ~54k spaces after the footer until max_tokens
    assert clean("Q.4 options\nMS" + " " * 54000, "length", PNG) == "Q.4 options\nMS\n"


def test_watermark_line_loop_is_stripped():
    # 2023 p1: "Joint Admission test for Masters" repeated until max_tokens, last copy cut
    wm = "Joint Admission test for Masters"
    out = clean("Q.1 text\n(D) option\n\n" + (wm + "\n") * 40 + "Joint Admission te", "length", PNG)
    assert out == "Q.1 text\n(D) option\n"


def test_few_repeats_still_raise():
    with pytest.raises(RuntimeError, match="truncated"):
        clean("Q.1 text\n(A) 1\n(A) 1\n(A) 1", "length", PNG)


def test_real_truncation_raises():
    with pytest.raises(RuntimeError, match="truncated"):
        clean("Q.1 a very long page cut mid-sen", "length", PNG)
