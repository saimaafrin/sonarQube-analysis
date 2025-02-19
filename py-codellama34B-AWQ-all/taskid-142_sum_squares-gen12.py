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

    
    # Base Case
    if not lst:
        return 0
    
    # Recursive Case
    else:
        if (lst.index(lst[0]) % 3 == 0) and (lst.index(lst[0]) % 4 == 0):
            lst[0] = lst[0]**2
        elif lst.index(lst[0]) % 3 == 0:
            lst[0] = lst[0]**3
        else:
            lst[0] = lst[0]
            
        return lst[0] + sum_squares(lst[1:])
