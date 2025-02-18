from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    size = len(l)
    mid = size // 2
    if size % 2 == 1:
        return l[mid]
    else:
        return (l[mid - 1] + l[mid]) / 2
