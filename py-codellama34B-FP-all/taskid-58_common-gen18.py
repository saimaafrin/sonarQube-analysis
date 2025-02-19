from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    l1.sort()
    l2.sort()
    i1 = 0
    i2 = 0
    com = []
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            i1 += 1
        elif l2[i2] < l1[i1]:
            i2 += 1
        else:
            com.append(l1[i1])
            i1 += 1
            i2 += 1
    return com
