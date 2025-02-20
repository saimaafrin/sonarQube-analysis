from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """


    # union of the two lists
    union_set = set(l1) | set(l2)

    # intersection of the two lists
    intersection_set = set(l1) & set(l2)

    # set difference to get elements that are in union but not intersection
    return sorted(list(union_set - intersection_set))
