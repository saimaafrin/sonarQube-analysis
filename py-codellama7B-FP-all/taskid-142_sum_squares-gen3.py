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

    
    # Define variables for the sum of squares, sum of cubes, and the length of the list
    sum_of_squares = 0
    sum_of_cubes = 0
    lst_length = len(lst)
    
    # For loop to iterate through each index of the list
    for i in range(0, lst_length):
        
        # If the index of the list is a multiple of 3
        if i % 3 == 0:
            
            # Square the integer at the index
            lst[i] = lst[i] ** 2
            
        # If the index of the list is a multiple of 4 and not a multiple of 3
        if i % 4 == 0 and i % 3 != 0:
            
            # Cube the integer at the index
            lst[i] = lst[i] ** 3
            
        # If the index of the list is a multiple of 3 or 4 but not a multiple of 3 and 4
        elif i % 3 == 0 or i % 4 == 0 and i % 3 != 0:
            
            # Do nothing
            pass
        
        # If the index of the list is not a multiple of 3, 4 or 7
        else:
            
            # Do nothing
            pass
        
    # Define the sum_of_squares variable
    sum_of_squares = sum(lst)
    
    # Return the sum of all the integers in the list
    return sum_of_squares
