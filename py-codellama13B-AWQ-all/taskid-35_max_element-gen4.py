from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 0:
        raise ValueError("empty list")
    result = l[0]
    for i in range(1, len(l)):
        if l[i] > result:
            result = l[i]
    return result
