from math_utils import add


def test_add_returns_sum():
    assert add(2, 3) == 5


def test_add_with_negatives():
    assert add(-1, 1) == 0
