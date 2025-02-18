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

    def reverse(arr):
        arr.reverse()
        return arr

    def digit2string(num: int):
        if num == 0:
            return 'Zero'
        elif num == 1:
            return 'One'
        elif num == 2:
            return 'Two'
        elif num == 3:
            return 'Three'
        elif num == 4:
            return 'Four'
        elif num == 5:
            return 'Five'
        elif num == 6:
            return 'Six'
        elif num == 7:
            return 'Seven'
        elif num == 8:
            return 'Eight'
        elif num == 9:
            return 'Nine'
        else:
            raise ValueError('Not a number between 1 and 9')

    # Write your code here
    return [digit2string(x) for x in reverse(sorted([x for x in arr if 1 <= x <= 9]))]
