from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    result = lst[0]
    for i in range(1, len(lst)):
        if i % 2 == 0:
            result += lst[i]
    return result
