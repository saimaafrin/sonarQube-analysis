from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    ret = 0
    for i, x in enumerate(lst):
        if x % 2 == 0 and i % 2 == 1:
            ret += x
    return ret
