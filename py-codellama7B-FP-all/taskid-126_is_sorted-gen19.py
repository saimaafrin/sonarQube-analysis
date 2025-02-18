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


    # Initialize a variable to check if there are duplicates
    duplicates = False

    # Iterate through the list
    for i in range(1, len(lst)):
        # Check if the current number is less than the previous one
        if lst[i] < lst[i - 1]:
            # If it is, return False
            return False
        # If the current number is the same as the previous one
        if lst[i] == lst[i - 1]:
            # Set the duplicates variable to True
            duplicates = True

    # Return True if no duplicates were found
    return not duplicates
