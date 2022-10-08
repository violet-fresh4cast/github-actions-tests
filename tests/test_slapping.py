"""Pytest tests."""
# import pytest

# from src.slapping.slap_that_like_button import LikeState, slap_many
from src.slapping.slap_that_like_button import add_two_number


def test_single_slap_disliked():
    """Test for adding numbers."""
    assert add_two_number(1, 1) == 2, "Basic maths failed"


# def test_empty_slap():
#     """Test for empty slap."""
#     assert slap_many(LikeState.empty, "") is LikeState.empty


# def test_single_slap_liked():
#     """Test for like button slap."""
#     assert slap_many(LikeState.empty, "l") is LikeState.liked


# def test_single_slap_disliked():
#     """Test for dislike button slap."""
#     assert slap_many(LikeState.empty, "d") is LikeState.disliked


# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         ("ll", LikeState.empty),
#         ("dd", LikeState.empty),
#         ("ld", LikeState.disliked),
#         ("dl", LikeState.liked),
#         ("ldd", LikeState.empty),
#         ("lldd", LikeState.empty),
#         ("ddl", LikeState.liked),
#     ],
# )
# def test_multi_slaps(test_input, expected):
#     assert slap_many(LikeState.empty, test_input) is expected


# @pytest.mark.skip(reason="regexes not supported yet")
# def test_regex_slaps():
#     assert slap_many(LikeState.empty, "[ld]*ddl") is LikeState.liked


# def test_invalid_slap():
#     with pytest.raises(ValueError):
#         slap_many(LikeState.empty, "x")


# def test_print(capture_stdout):
#     print("hello")
#     assert capture_stdout["stdout"] == "hello\n"
