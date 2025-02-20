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

    # Initialize the largest_negative and smallest_positive integers
    # as None
    largest_negative = None
    smallest_positive = None

    # Iterate over the list
    for num in lst:
        # If the num is negative and it is larger than the largest_negative
        # then make num the largest_negative
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num

        # If the num is positive and it is smaller than the smallest_positive
        # then make num the smallest_positive
        elif num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num

    # Return the largest_negative and smallest_positive integers
    # as a tuple
    return (largest_negative, smallest_positive)
