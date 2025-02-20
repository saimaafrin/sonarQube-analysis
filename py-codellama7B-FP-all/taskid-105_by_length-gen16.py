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


    def get_name(i: int) -> str:
        return "One" if i == 1 else "Two" if i == 2 else "Three" if i == 3 else "Four" if i == 4 else \
            "Five" if i == 5 else "Six" if i == 6 else "Seven" if i == 7 else "Eight" if i == 8 else "Nine"

    names = [get_name(i) for i in sorted(arr, reverse=True)]
    return names
