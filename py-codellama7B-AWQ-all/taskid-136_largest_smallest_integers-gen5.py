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

    smallest_positive: Optional[int] = None
    largest_negative: Optional[int] = None
    for element in lst:
        if element > 0:
            if smallest_positive is None:
                smallest_positive = element
            elif element < smallest_positive:
                smallest_positive = element
        elif element < 0:
            if largest_negative is None:
                largest_negative = element
            elif element > largest_negative:
                largest_negative = element
    return largest_negative, smallest_positive
