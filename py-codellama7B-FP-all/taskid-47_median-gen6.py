from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        # Median of two middle numbers is the average of the two middle numbers
        m = l[len(l) // 2 - 1] + l[len(l) // 2]
        return m / 2
