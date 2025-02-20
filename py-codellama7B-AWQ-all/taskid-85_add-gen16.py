from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    ans = 0
    for i in range(0, len(lst), 2):
        ans += lst[i]
    return ans
