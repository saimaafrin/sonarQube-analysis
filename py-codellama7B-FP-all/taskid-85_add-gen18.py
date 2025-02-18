from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    lst_even_idx_sum = 0
    for idx, element in enumerate(lst):
        if idx % 2 == 0:
            lst_even_idx_sum += element
    return lst_even_idx_sum
