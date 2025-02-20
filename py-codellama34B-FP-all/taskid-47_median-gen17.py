from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    n = len(l)
    if n % 2 == 0:
        # even number of elements
        return (sorted(l)[n // 2 - 1] + sorted(l)[n // 2]) / 2
    else:
        # odd number of elements
        return sorted(l)[n // 2]
