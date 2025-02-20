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

    arr = [str(x) for x in arr]
    arr.sort()
    arr.reverse()
    arr = [x if x == "1" else x if x == "2" else x if x == "3" else x if x == "4" else x if x == "5" else x if x == "6" else x if x == "7" else x if x == "8" else x if x == "9" else x for x in arr]
    return arr
