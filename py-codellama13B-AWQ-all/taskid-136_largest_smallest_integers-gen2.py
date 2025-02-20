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


    negative_list: List[int] = []
    positive_list: List[int] = []

    for num in lst:
        if num < 0:
            negative_list.append(num)
        elif num > 0:
            positive_list.append(num)

    if len(negative_list) == 0:
        negative_int = None
    else:
        negative_int = max(negative_list)

    if len(positive_list) == 0:
        positive_int = None
    else:
        positive_int = min(positive_list)

    return negative_int, positive_int
