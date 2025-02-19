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
    for num in lst:
        if num > 0:
            if smallest_positive is None:
                smallest_positive = num
            else:
                smallest_positive = min(smallest_positive, num)
        if num < 0:
            if largest_negative is None:
                largest_negative = num
            else:
                largest_negative = max(largest_negative, num)
    return largest_negative, smallest_positive
