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


    if len(l) == 1:
        return True

    last = l[0]
    increasing = l[0] < l[1]

    for elem in l[1:]:
        if elem == last:
            continue
        if (elem > last) == increasing:
            last = elem
        else:
            return False
    return True
