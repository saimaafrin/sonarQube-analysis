from typing import List

def monotonic(l: List[int]) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) < 3:
        return True

    diff_sign = 0
    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        if diff:
            if diff_sign == 0:
                diff_sign = diff
            elif diff_sign * diff < 0:
                return False

    return True
