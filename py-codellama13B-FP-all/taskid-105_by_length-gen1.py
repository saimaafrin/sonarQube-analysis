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

    for num in arr:
        if 1 <= num <= 9:
            result.append(num)

    result.sort(reverse=True)

    for i in range(len(result)):
        if result[i] == 1:
            result[i] = 'One'
        elif result[i] == 2:
            result[i] = 'Two'
        elif result[i] == 3:
            result[i] = 'Three'
        elif result[i] == 4:
            result[i] = 'Four'
        elif result[i] == 5:
            result[i] = 'Five'
        elif result[i] == 6:
            result[i] = 'Six'
        elif result[i] == 7:
            result[i] = 'Seven'
        elif result[i] == 8:
            result[i] = 'Eight'
        elif result[i] == 9:
            result[i] = 'Nine'

    return result
