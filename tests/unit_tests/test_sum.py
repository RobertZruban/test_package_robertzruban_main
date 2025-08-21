# test_sum_utils.py
import math
import pytest

from test_package_robertzruban_main.sum_utils import add

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (1, 2, 3.0),
        (-5, 5, 0.0),
        (2.5, 0.5, 3.0),
        (1e18, 1e18, 2e18),
        (True, 2, 3.0),         # bools are valid SupportsFloat
        ("3.5", "1.5", 5.0),    # strings convertible to float also work
    ],
)
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_commutative():
    x, y = 1.23, 4.56
    assert add(x, y) == add(y, x)

def test_add_with_nan():
    # If any operand is NaN (after float conversion), result should be NaN
    res = add(float("nan"), 1)
    assert math.isnan(res)

def test_add_with_inf():
    assert add(float("inf"), 1) == float("inf")
    assert add(float("-inf"), -1) == float("-inf")

def test_add_typeerror_on_unconvertible():
    class NotFloatable:
        pass

    with pytest.raises(TypeError):
        _ = add(NotFloatable(), 1)
