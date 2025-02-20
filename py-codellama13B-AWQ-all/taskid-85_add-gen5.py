from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """


    return sum([item for idx, item in enumerate(lst) if idx % 2 == 0 and item % 2 == 0])
