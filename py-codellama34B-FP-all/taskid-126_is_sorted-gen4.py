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


    # We want to compare each element to the element before it. If we
    # compare the first element to some non-existant element before
    # it, we'll get an error. So we start at the second element,
    # element 1.
    for i in range(1, len(lst)):
        # If the current element is less than the element before it,
        # we know the list isn't sorted.
        if lst[i] < lst[i - 1]:
            return False

        # If the current element is equal to the element before it,
        # and the element before that is equal as well, then we have
        # duplicates.
        if lst[i] == lst[i - 1] and lst[i - 1] == lst[i - 2]:
            return False

    # If we get through all elements without returning False, we know
    # the list is sorted.
    return True
