from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        half = len(l) // 2
        return (l[half - 1] + l[half]) / 2
