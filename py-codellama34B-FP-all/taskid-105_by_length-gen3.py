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

    one_to_nine = [
        "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"
    ]

    filtered = [i for i in arr if 1 <= i <= 9]
    sorted_filtered = sorted(filtered, reverse=True)
    return [one_to_nine[i - 1] for i in sorted_filtered]
