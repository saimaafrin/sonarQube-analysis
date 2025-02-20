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

    lst_negative = list(filter(lambda x: x < 0, lst))
    if len(lst_negative) != 0:
        largest_negative = max(lst_negative)
    else:
        largest_negative = None

    lst_positive = list(filter(lambda x: x > 0, lst))
    if len(lst_positive) != 0:
        smallest_positive = min(lst_positive)
    else:
        smallest_positive = None

    return (largest_negative, smallest_positive)
\end{code}
