from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    size = len(l)
    if size == 0:
        return 0.0
    elif size % 2 == 1:
        return l[size//2]
    else:
        return (l[size//2 - 1] + l[size//2])/2
