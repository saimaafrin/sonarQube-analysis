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

    str_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    length = len(arr)
    if length == 0:
        return []
    elif length == 1:
        return [str_list[arr[0] - 1]]
    else:
        new_list = []
        for i in range(length):
            if 1 <= arr[i] <= 9:
                new_list.append(str_list[arr[i] - 1])
        new_list.reverse()
        return new_list
