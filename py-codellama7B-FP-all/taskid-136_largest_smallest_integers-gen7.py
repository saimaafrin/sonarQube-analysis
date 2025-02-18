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

    neg_integers, pos_integers = [], []
    for x in lst:
        if x < 0:
            neg_integers.append(x)
        else:
            pos_integers.append(x)

    neg_integers.sort(reverse=True)
    pos_integers.sort()

    return neg_integers[0] if neg_integers else None, pos_integers[0] if pos_integers else None
