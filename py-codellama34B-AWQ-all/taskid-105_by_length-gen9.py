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

    def get_name(n):
        if n == 1: return "One"
        if n == 2: return "Two"
        if n == 3: return "Three"
        if n == 4: return "Four"
        if n == 5: return "Five"
        if n == 6: return "Six"
        if n == 7: return "Seven"
        if n == 8: return "Eight"
        if n == 9: return "Nine"
        return ""

    return list(map(get_name, sorted(filter(lambda x: 1 <= x <= 9, arr), reverse=True)))
