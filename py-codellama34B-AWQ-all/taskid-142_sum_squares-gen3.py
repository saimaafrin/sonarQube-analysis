from typing import List

def sum_squares(lst: List[int]) -> int:
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    >>> lst
    [1, 2, 3]
    >>> lst
    []
    >>> lst
    [-1, -5, 2, -1, -5]
    """

    # loop through list to see if index is a multiple of 3 and or 4
    for index in range(len(lst)):
        # if index is a multiple of 3, square entry
        if index % 3 == 0:
            lst[index] = lst[index]**2
        # if index is a multiple of 4, cube entry
        elif index % 4 == 0:
            lst[index] = lst[index]**3

    # return sum of entries
    return sum(lst)
