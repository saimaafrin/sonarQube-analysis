from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """

    # Get the unique values in the list
    unique_values = set(lst)
    # Set the maximum value to return to -1
    maximum = -1
    # Loop through the unique values
    for value in unique_values:
        # Get the frequency of the value in the list
        frequency = lst.count(value)
        # Check if the frequency of the value is greater than or equal to the value
        if frequency >= value and value > maximum:
            # Update the maximum
            maximum = value
    return maximum
