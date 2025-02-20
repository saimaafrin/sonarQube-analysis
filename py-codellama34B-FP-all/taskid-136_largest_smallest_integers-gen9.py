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


    neg_max: Optional[int] = None
    pos_min: Optional[int] = None

    for item in lst:
        if item < 0:
            neg_max = max(neg_max, item)
        elif item > 0:
            pos_min = min(pos_min, item)

    return neg_max, pos_min
