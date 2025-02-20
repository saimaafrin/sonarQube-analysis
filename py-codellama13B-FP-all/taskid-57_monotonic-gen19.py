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

    n = len(l)
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        a = l[0]
        for i in range(1, n):
            if a > l[i] and a >= l[i] or a < l[i] and a <= l[i]:
                return False
            a = l[i]
        return True
