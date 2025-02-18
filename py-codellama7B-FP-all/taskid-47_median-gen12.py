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
        # Odd number of elements.
        return l[len(l) // 2]
    else:
        # Even number of elements.
        i = len(l) // 2
        return (l[i - 1] + l[i]) / 2
