from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] + lst[1]
    if len(lst) == 3:
        return lst[0] + lst[1] + lst[2]
    if len(lst) == 4:
        return lst[0] + lst[1] + lst[2] + lst[3]
    if len(lst) == 5:
        return lst[0] + lst[1] + lst[2] + lst[3] + lst[4]

    res = lst[0] + lst[2]
    for i in range(4, len(lst), 2):
        res += lst[i]
    return res
