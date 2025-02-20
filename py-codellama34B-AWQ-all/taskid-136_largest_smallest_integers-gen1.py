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

    negative = []
    positive = []
    for element in lst:
        if element < 0:
            negative.append(element)
        elif element > 0:
            positive.append(element)
    negative.sort(reverse=True)
    positive.sort()
    return (negative[0] if negative else None, positive[0] if positive else None)
