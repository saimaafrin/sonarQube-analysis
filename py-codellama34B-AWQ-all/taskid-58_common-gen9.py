from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    if not l1 or not l2:
        return []

    l1 = sorted(set(l1))
    l2 = sorted(set(l2))
    i = j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            res.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return res
