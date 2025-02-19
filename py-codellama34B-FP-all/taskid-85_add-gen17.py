from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    res = 0
    for index, item in enumerate(lst):
        if index % 2 != 0:
            res += item
    return res
