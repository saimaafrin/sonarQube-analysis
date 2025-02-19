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

    # Find the frequency of each number in the list
    number_frequencies = {}
    for number in lst:
        if number in number_frequencies:
            number_frequencies[number] += 1
        else:
            number_frequencies[number] = 1

    # Find the largest number that has a frequency greater than the number itself
    largest_number = 0
    for number, frequency in number_frequencies.items():
        if frequency > number and frequency > largest_number:
            largest_number = frequency

    # If no number satisfies the condition, return -1
    if largest_number == 0:
        return -1

    # Otherwise, return the largest number
    return largest_number
