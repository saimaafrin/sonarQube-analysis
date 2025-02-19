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

    
    # Check if list is empty
    if len(lst) == 0:
        return 0
    
    # Loop through the list
    for i in range(len(lst)):
        
        # Check if index is a multiple of 3
        if i % 3 == 0:
            
            # Square the number
            lst[i] = lst[i]**2
            
        # Check if index is a multiple of 4
        if i % 4 == 0:
            
            # Cube the number
            lst[i] = lst[i]**3
            
    # Return the sum
    return sum(lst)
