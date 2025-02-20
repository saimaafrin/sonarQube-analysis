from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # create a set of elements in l1 and l2
    set_l1 = set(l1)
    set_l2 = set(l2)
    
    # find the intersection
    common_elements = set_l1.intersection(set_l2)
    
    # return sorted list
    return sorted(list(common_elements))
