from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    """


    # Even Positions
    # 1) 0, 2, 4, 6 ... 
    # 2) 1, 3, 5, 7 ...
    
    # Odd Positions
    # 1) 1, 3, 5, 7 ...
    # 2) 2, 4, 6, 8 ...

    # Odd elements in even positions
    # 1) 1, 3, 5, 7 ...
    # 2) 2, 4, 6, 8 ...

    # Even Positions
    # 1) 0, 2, 4, 6 ... 
    # 2) 1, 3, 5, 7 ...
    # Odd Positions
    # 1) 1, 3, 5, 7 ...
    # 2) 2, 4, 6, 8 ...

    result = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            result += lst[i]

    return result
