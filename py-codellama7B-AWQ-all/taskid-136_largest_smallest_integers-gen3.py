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

    negative_integer = None
    positive_integer = None
    for i in lst:
        if i < 0:
            if negative_integer is None:
                negative_integer = i
        elif i > 0:
            if positive_integer is None:
                positive_integer = i
        if negative_integer is not None and positive_integer is not None:
            break
    return negative_integer, positive_integer
