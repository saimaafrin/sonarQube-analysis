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

    # This solution is in O(n) time and O(n) space.
    # We could also solve it in O(n) time and O(1) space.

    # We create a hash map of frequencies.
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # We check if there are any numbers that have a frequency greater than or equal to the number itself.
    for num, freq in frequency.items():
        if freq >= num:
            return num
    
    # If there are no such numbers, return -1.
    return -1
