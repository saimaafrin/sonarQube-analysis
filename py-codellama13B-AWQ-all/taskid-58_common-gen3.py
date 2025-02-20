from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    res = []
    for i in l1:
        if i in l2:
            if i not in res:
                res.append(i)
    for j in l2:
        if j not in l1:
            if j not in res:
                res.append(j)
    return sorted(res)
