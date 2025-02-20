from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    # if not lst:
    #     return 0
    # sum_evens = 0
    # for index, value in enumerate(lst):
    #     if index % 2 == 0:
    #         if value % 2 == 0:
    #             sum_evens += value
    # return sum_evens
    return sum(filter(lambda x: x % 2 == 0 and index % 2 == 0, lst))
