from typing import List

def unique(l: List[int]) -> List[int]:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            l.pop(i+1)
    return l
