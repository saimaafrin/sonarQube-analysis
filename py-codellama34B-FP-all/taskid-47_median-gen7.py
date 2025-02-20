from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    l_len = len(l)
    if l_len % 2 == 0:
        return (l[l_len // 2 - 1] + l[l_len // 2]) / 2
    else:
        return l[l_len // 2]
