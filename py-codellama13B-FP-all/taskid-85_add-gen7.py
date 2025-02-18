from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    sum_ = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 != 0:
            sum_ += num
    return sum_
