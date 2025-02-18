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

    diff = [l[i+1] - l[i] for i in range(len(l) - 1)]
    if diff[0] < 0:
        return all(d <= 0 for d in diff)
    return all(d >= 0 for d in diff)
