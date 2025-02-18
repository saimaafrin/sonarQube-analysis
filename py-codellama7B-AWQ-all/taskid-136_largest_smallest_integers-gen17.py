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

    # This is how you'd solve this using the built-in sort.
    # lst.sort()
    # largest_negative = lst[0] if lst[0] < 0 else None
    # smallest_positive = lst[-1] if lst[-1] > 0 else None
    # return (largest_negative, smallest_positive)

    # This is how you'd solve this using a for loop.
    largest_negative = None
    smallest_positive = None
    for i in lst:
        if i < 0 and (largest_negative is None or i > largest_negative):
            largest_negative = i
        if i > 0 and (smallest_positive is None or i < smallest_positive):
            smallest_positive = i
    return (largest_negative, smallest_positive)
