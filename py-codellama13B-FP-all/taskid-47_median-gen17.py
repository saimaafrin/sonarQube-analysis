from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """


    if not l:
        raise ValueError('median requires at least one element.')
    l.sort()
    size = len(l)
    half = size // 2
    return l[half] if size % 2 == 1 else (l[half-1] + l[half]) / 2
