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


    # Create a dictionary where key is the number and value is frequency of it
    # The frequency of each number will be stored in a dictionary
    frequency_map = {}
    for num in lst:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    # Find the number with the maximum frequency which is greater than or equal to the number itself
    max_value = -1
    for num, freq in frequency_map.items():
        if freq >= num and freq > max_value:
            max_value = freq

    return max_value
