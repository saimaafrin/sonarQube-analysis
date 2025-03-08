from typing import List

def sum_squares(lst: List[float]) -> int:
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    >>> lst([1.0, 2.0, 3.0])
    14
    >>> lst([1.0, 4.0, 9.0])
    98
    >>> lst([1.0, 3.0, 5.0, 7.0])
    84
    >>> lst([1.4, 4.2, 0.0])
    29
    >>> lst([-2.4, 1.0, 1.0])
    6
    

    """

    return sum([int(x**2) for x in lst])
