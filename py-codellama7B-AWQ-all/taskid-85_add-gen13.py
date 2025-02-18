from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    # TODO - you fill in here.
    return sum([x for i, x in enumerate(lst) if i % 2 == 1])
