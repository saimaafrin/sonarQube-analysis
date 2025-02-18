from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
    (None, 1)
    >>> largest_smallest_integers([])
    (None, None)
    >>> largest_smallest_integers([0])
    (None, None)
    """

    lst.sort()
    neg_max = None
    pos_min = None
    for i in lst:
        if i < 0 and (neg_max is None or neg_max < i):
            neg_max = i
        elif i > 0 and (pos_min is None or pos_min > i):
            pos_min = i
    return (neg_max, pos_min)
