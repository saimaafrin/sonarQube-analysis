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

    positive_list = []
    negative_list = []

    for i in lst:
        if i >= 0:
            positive_list.append(i)
        else:
            negative_list.append(i)

    if len(positive_list) == 0:
        return (None, min(negative_list, default=None))

    if len(negative_list) == 0:
        return (max(positive_list, default=None), None)

    return (max(negative_list), min(positive_list))
