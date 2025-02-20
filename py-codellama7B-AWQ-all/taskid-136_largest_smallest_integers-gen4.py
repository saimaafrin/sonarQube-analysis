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


    # TODO: Write your solution here
    # HINT: Create a flag variable to store the largest negative
    #       integer you encounter, and create a second flag variable
    #       to store the smallest positive integer you encounter.
    #       If the flag variables are None, then you haven't
    #       encountered a negative or positive integer yet,
    #       respectively.
    #       Use two nested loops to iterate through the input list.
    #       In the first loop, check if the current integer is
    #       negative. If it is, set the 'largest_negative' flag
    #       variable to the current integer if it is smaller than
    #       the 'largest_negative' flag variable.
    #       In the second loop, check if the current integer is
    #       positive. If it is, set the 'smallest_positive' flag
    #       variable to the current integer if it is greater than
    #       the 'smallest_positive' flag variable.

    largest_negative = None
    smallest_positive = None
    for i in lst:
        if i < 0:
            if largest_negative == None or i > largest_negative:
                largest_negative = i
        else:
            if smallest_positive == None or i < smallest_positive:
                smallest_positive = i
    return (largest_negative, smallest_positive)
