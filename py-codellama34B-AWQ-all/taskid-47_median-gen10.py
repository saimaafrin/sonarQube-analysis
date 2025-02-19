from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    if len(l) == 0:
        return 0
    l.sort()
    if len(l) % 2 == 0:
        # even
        return (l[int(len(l)/2)-1] + l[int(len(l)/2)]) / 2
    else:
        # odd
        return l[int(len(l)/2)]
