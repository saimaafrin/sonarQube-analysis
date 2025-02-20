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

    res = []
    for num in arr:
        if 1 <= num <= 9:
            res.append(num)
    res.sort()
    res.reverse()
    res = [str(i) for i in res]
    res = [i.replace('1', 'One').replace('2', 'Two').replace('3', 'Three').replace('4', 'Four')
     .replace('5', 'Five').replace('6', 'Six').replace('7', 'Seven').replace('8', 'Eight').replace('9', 'Nine')
     for i in res]
    return res
