from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) == 0:
        raise ValueError("median of empty list")
    l = sorted(l)
    i = len(l) // 2
    if len(l) % 2 == 1:
        return l[i]
    else:
        return (l[i-1] + l[i]) / 2.0
