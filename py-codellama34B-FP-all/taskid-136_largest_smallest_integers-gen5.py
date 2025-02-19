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


    # Initialize variables
    largest_negative: int = None
    smallest_positive: int = None

    # Iterate through list
    for num in lst:
        # Check if negative
        if num < 0 and (largest_negative == None or num > largest_negative):
            largest_negative = num
        # Check if positive
        elif num > 0 and (smallest_positive == None or num < smallest_positive):
            smallest_positive = num
    
    # Return tuple
    return (largest_negative, smallest_positive)
