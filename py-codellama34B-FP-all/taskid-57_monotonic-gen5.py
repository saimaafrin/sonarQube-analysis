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

    inc = False
    dec = False
    if len(l) < 2:
        return True
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            if dec:
                return False
            inc = True
        elif l[i] > l[i + 1]:
            if inc:
                return False
            dec = True
        else:
            pass
    return True
