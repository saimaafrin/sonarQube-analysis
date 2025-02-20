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

    # Edge case
    if len(lst) == 1:
        return True
    # Set up initial values
    previous = lst[0]
    for i in range(1, len(lst)):
        current = lst[i]
        # If duplicate is detected, return False
        if current == previous:
            if lst[i+1:] and current == lst[i+1]:
                return False
        # Check if list is sorted
        if current < previous:
            return False
        previous = current
    return True
