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

    # initialize variables
    last_element = None
    duplicates_count = 0
    duplicates = False

    # loop through list and check if list is sorted
    for element in lst:
        if last_element and element == last_element:
            duplicates_count += 1
        else:
            duplicates_count = 0

        if duplicates_count > 1:
            duplicates = True

        last_element = element

    return not duplicates
