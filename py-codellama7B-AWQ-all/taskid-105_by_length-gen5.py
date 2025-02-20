from typing import List

def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    
      If the array is empty, return an empty array:
    >>> by_length([])
    []
    
      If the array has any strange number ignore it:
    >>> by_length([1, -1, 55])
    ['One']
    """

    # Create a list of the numbers that are between 1 and 9.
    numbers = [number for number in arr if 1 <= number <= 9]

    # Sort the list of numbers in ascending order.
    numbers.sort()

    # Reverse the list of numbers.
    numbers.reverse()

    # Create a list of the names of the numbers.
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    # Replace each number in the list with its corresponding name.
    result = [names[number - 1] for number in numbers]

    return result
