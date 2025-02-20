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

    negative_integers: List[int] = [x for x in lst if x < 0]
    positive_integers: List[int] = [x for x in lst if x >= 0]

    if len(negative_integers) == 0:
        largest_negative = None
    else:
        largest_negative = max(negative_integers)

    if len(positive_integers) == 0:
        smallest_positive = None
    else:
        smallest_positive = min(positive_integers)

    return largest_negative, smallest_positive
