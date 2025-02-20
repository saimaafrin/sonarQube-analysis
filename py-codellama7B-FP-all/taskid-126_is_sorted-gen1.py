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

    # If list is empty or has only 1 element, return True.
    if len(lst) < 2:
        return True

    # Iterate through list and keep track of duplicate counts.
    duplicate_counts = {}
    for num in lst:
        if num in duplicate_counts:
            duplicate_counts[num] += 1
        else:
            duplicate_counts[num] = 1

    # If there are any duplicates, return False.
    if len(duplicate_counts) > 1:
        return False

    # If list is sorted, return True.
    return sorted(lst) == lst
