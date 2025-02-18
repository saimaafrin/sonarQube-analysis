from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    sorted_l = sorted(l)
    if len(sorted_l) % 2 == 1:
        return sorted_l[len(sorted_l) // 2]
    else:
        return (sorted_l[len(sorted_l) // 2 - 1] + sorted_l[len(sorted_l) // 2]) / 2
