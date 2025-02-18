from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    m = len(l)
    if m % 2:
        return l[m // 2]
    else:
        return (l[m // 2] + l[m // 2 - 1]) / 2
