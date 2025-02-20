from typing import List

def unique(l: List[int]) -> List[int]:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    l.sort()
    unique_list = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i-1]:
            unique_list.append(l[i])
    return unique_list
