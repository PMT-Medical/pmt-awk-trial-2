from math_utils import add, multiply


def test_add_returns_sum():
    assert add(2, 3) == 5


def test_add_with_negatives():
    assert add(-1, 1) == 0


def test_multiply_returns_product():
    assert multiply(3, 4) == 12
