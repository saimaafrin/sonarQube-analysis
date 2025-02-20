from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    total = 0
    for idx, element in enumerate(lst):
        if element % 2 == 0 and idx % 2 == 1:
            total += element
    return total
