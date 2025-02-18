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

    if len(l) <= 1:
        return True

    last = l[0]
    for i in range(1, len(l)):
        if l[i] == last:
            continue

        if l[i] < last:
            if any(l[i] < x for x in l[:i]):
                return False
        elif l[i] > last:
            if any(l[i] > x for x in l[:i]):
                return False

        last = l[i]

    return True
