"""Pytest tests."""
import pytest

from src.flapping.flap_that_like_button import (
    LikeState,
    add_two_number_extra,
    flap_many,
)


def test_maths():
    """Test for adding numbers."""
    assert add_two_number_extra(3, 2) == 5, "Basic maths failed"


def test_empty_flap():
    """Test for empty flap."""
    assert flap_many(LikeState.empty, "") is LikeState.empty


def test_single_flap_liked():
    """Test for like button flap."""
    assert flap_many(LikeState.empty, "l") is LikeState.liked


def test_single_flap_disliked():
    """Test for dislike button flap."""
    assert flap_many(LikeState.empty, "d") is LikeState.disliked


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("ll", LikeState.empty),
        ("dd", LikeState.empty),
        ("ld", LikeState.disliked),
        ("dl", LikeState.liked),
        ("ldd", LikeState.empty),
        ("lldd", LikeState.empty),
        ("ddl", LikeState.liked),
    ],
)
def test_multi_flaps(test_input, expected):
    assert flap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_flaps():
    assert flap_many(LikeState.empty, "[ld]*ddl") is LikeState.liked


def test_invalid_flap():
    with pytest.raises(ValueError):
        flap_many(LikeState.empty, "x")


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
