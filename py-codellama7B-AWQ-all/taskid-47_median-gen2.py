from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    mid = len(l) / 2
    if not isinstance(mid, int):
        return (l[int(mid)] + l[int(mid) - 1]) / 2
    return l[int(mid)]
