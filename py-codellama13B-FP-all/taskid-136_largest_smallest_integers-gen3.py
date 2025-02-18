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

    largest_negative_int = None
    smallest_positive_int = None
    for x in lst:
        if x < 0:
            if largest_negative_int == None:
                largest_negative_int = x
            elif x > largest_negative_int:
                largest_negative_int = x
        if x > 0:
            if smallest_positive_int == None:
                smallest_positive_int = x
            elif x < smallest_positive_int:
                smallest_positive_int = x
    return (largest_negative_int, smallest_positive_int)
