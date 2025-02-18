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

    pos_int = None
    neg_int = None
    for i in lst:
        if i > 0:
            if pos_int is None or i > pos_int:
                pos_int = i
        elif i < 0:
            if neg_int is None or i < neg_int:
                neg_int = i
    return neg_int, pos_int
