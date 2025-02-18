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

    for number in lst:
        if number > 0 and (smallest_positive is None or number < smallest_positive):
            smallest_positive = number
        elif number < 0 and (largest_negative is None or number > largest_negative):
            largest_negative = number

    return largest_negative, smallest_positive
