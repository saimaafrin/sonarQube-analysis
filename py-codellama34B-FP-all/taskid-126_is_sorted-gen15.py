from typing import List

def is_sorted(lst: List[int]) -> bool:
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    >>> is_sorted([5])
    True
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1, 3, 2, 4, 5])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 6])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7])
    True
    >>> is_sorted([1, 3, 2, 4, 5, 6, 7])
    False
    >>> is_sorted([1, 2, 2, 3, 3, 4])
    True
    >>> is_sorted([1, 2, 2, 2, 3, 4])
    False
    """

    # edge case: list is empty
    if not lst:
        return True

    # edge case: list has only one element
    if len(lst) == 1:
        return True

    # edge case: list has only one repeated element
    if len(lst) == 2 and lst[0] == lst[1]:
        return True

    # edge case: list has consecutive duplicates
    if len(lst) > 2 and lst[0] == lst[1] and lst[1] == lst[2]:
        return False

    # normal cases
    if lst[0] < lst[1]:
        return is_sorted(lst[1:])
    else:
        return False
