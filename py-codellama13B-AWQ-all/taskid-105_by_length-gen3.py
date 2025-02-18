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

    length = 9
    result = []
    for num in arr:
        if 1 <= num <= length:
            result.append(num)
    result.sort(reverse=True)
    result = [f"{num}" for num in result]
    for i, val in enumerate(result):
        result[i] = result[i].replace(str(val), "One")
        if val == "Two":
            result[i] = result[i].replace(str(val), "Two")
        elif val == "Three":
            result[i] = result[i].replace(str(val), "Three")
        elif val == "Four":
            result[i] = result[i].replace(str(val), "Four")
        elif val == "Five":
            result[i] = result[i].replace(str(val), "Five")
        elif val == "Six":
            result[i] = result[i].replace(str(val), "Six")
        elif val == "Seven":
            result[i] = result[i].replace(str(val), "Seven")
        elif val == "Eight":
            result[i] = result[i].replace(str(val), "Eight")
        elif val == "Nine":
            result[i] = result[i].replace(str(val), "Nine")
    return result
