from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    if len(lst) == 0:
        return 0
    even_sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum
