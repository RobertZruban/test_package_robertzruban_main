# sum_utils.py
from typing import SupportsFloat


def add(a: SupportsFloat, b: SupportsFloat) -> float:
    """
    Return the arithmetic sum of two numeric values.

    This function accepts any values that can be converted to float (e.g., int, float, numpy scalar).

    Args:
        a: The first addend. Must support conversion to float (i.e., implement __float__()).
        b: The second addend. Must support conversion to float.

    Returns:
        The sum of `a` and `b` as a float.

    Examples:
        >>> add(2, 3)
        5.0
        >>> add(2.5, 0.5)
        3.0
        >>> add(True, 2)  # bool is SupportsFloat (True -> 1.0)
        3.0
    """
    return float(a) + float(b)
