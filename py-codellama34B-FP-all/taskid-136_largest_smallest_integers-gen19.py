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

    neg_lst = list()
    pos_lst = list()
    for item in lst:
        if item < 0:
            neg_lst.append(item)
        elif item > 0:
            pos_lst.append(item)

    if neg_lst:
        max_neg = max(neg_lst)
    else:
        max_neg = None

    if pos_lst:
        min_pos = min(pos_lst)
    else:
        min_pos = None

    return (max_neg, min_pos)
