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
    delta = l[0] - l[1]
    for i in range(1, len(l) - 1):
        d = l[i] - l[i + 1]
        if d == 0:
            continue
        if delta == 0:
            delta = d
        elif delta * d < 0:
            return False
    return True
