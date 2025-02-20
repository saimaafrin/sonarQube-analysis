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

    largest_negative_integer = None
    smallest_positive_integer = None

    for element in lst:
        if element < 0 and (largest_negative_integer is None or element > largest_negative_integer):
            largest_negative_integer = element
        elif element > 0 and (smallest_positive_integer is None or element < smallest_positive_integer):
            smallest_positive_integer = element
    
    return largest_negative_integer, smallest_positive_integer
