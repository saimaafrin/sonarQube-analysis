from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """


    if not lst:
        return 0
    return sum(lst[i] for i in range(len(lst)) if i % 2)
