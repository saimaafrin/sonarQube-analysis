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


    # Dictionary to keep track of the frequencies of the elements in the list
    frequency_dict = {}

    # Iterate through each element in the list and increase the frequency by 1
    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    # Get the maximum element from the dictionary by value
    max_value = max(frequency_dict.values())

    # Iterate through each key value pair in the dictionary
    for key, value in frequency_dict.items():

        # If the value is equal to the maximum value and key is greater than zero, return key
        if value == max_value and key > 0:
            return key

    # If no such a value exist, return -1
    return -1
