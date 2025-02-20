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

    if len(l) < 2:
        return True

    # If first two elements are the same, all others must be same.
    if l[0] == l[1]:
        return all(l[i] == l[i+1] for i in range(len(l) - 1))

    increasing = l[0] < l[1]

    for i in range(len(l) - 1):
        if increasing and l[i] > l[i+1]:
            return False
        if not increasing and l[i] < l[i+1]:
            return False

    return True
