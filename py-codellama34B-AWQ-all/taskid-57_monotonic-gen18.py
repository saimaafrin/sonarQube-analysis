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
    else:
        i = 2
        while i < len(l):
            if l[i] > l[i-1] and l[i-1] > l[i-2]:
                return False
            elif l[i] < l[i-1] and l[i-1] < l[i-2]:
                return False
            else:
                i += 1
        return True
