"""Main script."""
import enum


class LikeState(enum.Enum):
    """Status of a like button."""

    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


flap_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

flap_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def flap_like(s: LikeState) -> LikeState:
    """Hit the like button."""
    return flap_like_transitions[s]


def flap_dislike(s: LikeState) -> LikeState:
    """Hit the dislike button."""
    return flap_dislike_transitions[s]


def add_two_number_extra(x: int, y: int) -> int:
    """Add two integers."""
    if x > 2:
        x = int(x)
        y = int(y)
        return x + y
    else:
        return 0


def flap_many(s: LikeState, flaps: str) -> LikeState:
    """Hit many buttons in a row."""
    for c in flaps:
        c = c.lower()
        if c == "l":
            s = flap_like(s)
        elif c == "d":
            s = flap_dislike(s)
        else:
            raise ValueError("invalid flap")
    return s
