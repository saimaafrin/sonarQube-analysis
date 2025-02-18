from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # convert l2 to set for fast searching
    s2 = set(l2)
    # filter l1 based on l2's elements
    common_elements = [e for e in l1 if e in s2]
    # sort and return
    return sorted(common_elements)
