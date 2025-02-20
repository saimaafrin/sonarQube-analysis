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

    pos_min = None
    neg_max = None

    for num in lst:
        if num > 0:
            if pos_min is None:
                pos_min = num
            else:
                pos_min = min(pos_min, num)
        elif num < 0:
            if neg_max is None:
                neg_max = num
            else:
                neg_max = max(neg_max, num)

    return (neg_max, pos_min)
