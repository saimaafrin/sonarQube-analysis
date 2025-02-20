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

    # Solution 1:
    # def sum_squares(lst: List[int]) -> int:
    #     # return sum([i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for j, i in enumerate(lst)])
    #     return sum(i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for j, i in enumerate(lst))
    # Solution 2:
    return sum(i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for j, i in enumerate(lst))

    # Solution 3:
    # return sum(i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for j, i in enumerate(lst))
    # return sum(i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for i, j in enumerate(lst))
    # Solution 4:
    # return sum([i**(3 if j % 3 == 0 else 4 if j % 4 == 0 else 1) for j, i in enumerate(lst)])
