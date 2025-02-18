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

    result = []
    for item in arr:
        if 1 <= item <= 9:
            result.append(item)
    result.sort()
    result.reverse()
    result = [str(i) for i in result]
    result = [{'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}[i] for i in result]
    return result
