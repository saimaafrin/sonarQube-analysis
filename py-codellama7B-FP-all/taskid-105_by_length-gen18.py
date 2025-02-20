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

    if not arr:
        return []

    arr.sort()
    arr.reverse()

    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    for i in range(len(arr)):
        if arr[i] < 1 or arr[i] > 9:
            continue
        arr[i] = names[arr[i]-1]

    return arr
