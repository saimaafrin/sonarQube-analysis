from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    sorted_list = sorted(l)
    size = len(sorted_list)
    if size % 2 == 0:
        return (sorted_list[size//2 - 1] + sorted_list[size//2]) / 2
    return sorted_list[size//2]
