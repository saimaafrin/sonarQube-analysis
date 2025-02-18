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

    # your code here
    res = []
    for i in range(len(arr)):
        if arr[i] >= 1 and arr[i] <= 9:
            res.append(arr[i])
    res.sort(reverse=True)
    for i in range(len(res)):
        res[i] = str(res[i])
    for i in range(len(res)):
        if res[i] == '1':
            res[i] = 'One'
        elif res[i] == '2':
            res[i] = 'Two'
        elif res[i] == '3':
            res[i] = 'Three'
        elif res[i] == '4':
            res[i] = 'Four'
        elif res[i] == '5':
            res[i] = 'Five'
        elif res[i] == '6':
            res[i] = 'Six'
        elif res[i] == '7':
            res[i] = 'Seven'
        elif res[i] == '8':
            res[i] = 'Eight'
        elif res[i] == '9':
            res[i] = 'Nine'
    return res
