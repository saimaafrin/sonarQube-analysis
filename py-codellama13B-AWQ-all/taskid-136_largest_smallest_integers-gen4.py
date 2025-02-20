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

    smallest_positive = None
    largest_negative = None

    for i in lst:
        if i > 0:
            if smallest_positive == None:
                smallest_positive = i
            else:
                if i < smallest_positive:
                    smallest_positive = i
        elif i < 0:
            if largest_negative == None:
                largest_negative = i
            else:
                if i > largest_negative:
                    largest_negative = i

    return (largest_negative, smallest_positive)
