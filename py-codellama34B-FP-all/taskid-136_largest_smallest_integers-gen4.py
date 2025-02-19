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

    for num in lst:
        if num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num

    return largest_negative, smallest_positive
