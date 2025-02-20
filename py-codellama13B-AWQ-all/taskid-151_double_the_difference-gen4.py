from typing import List

def double_the_difference(lst: List[float]) -> int:
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    >>> double_the_difference([1, 3, 2, 0])
    10
    >>> double_the_difference([-1, -2, 0])
    0
    >>> double_the_difference([9, -2])
    81
    >>> double_the_difference([0])
    0
   
    If the input list is empty, return 0.
    """

    odd_squares = 0
    for number in lst:
        if int(number) * int(number) % 2 == 1:
            odd_squares += int(number) * int(number)
    return odd_squares
    
    # return sum(int(number)**2 for number in lst if int(number) % 2 == 1)
    
    # return sum(map(lambda x: x**2, filter(lambda x: x % 2 == 1, lst)))
    
    # return sum(x**2 for x in lst if x % 2 == 1)
