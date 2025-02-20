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

    if len(l) < 2: return True
    if l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i] < l[i-1]: return False
    else:
        for i in range(1, len(l)):
            if l[i] > l[i-1]: return False
    return True
