from typing import List

def incr_list(l: List[int]) -> List[int]:
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """


    result: List[int] = []
    for i in l:
        result.append(i + 1)
    return result
