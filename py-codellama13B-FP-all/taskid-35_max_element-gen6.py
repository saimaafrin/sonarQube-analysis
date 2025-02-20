from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 0:
        raise ValueError('cannot find the maximum element in an empty list')
    max_value = l[0]
    for i in range(1, len(l)):
        if l[i] > max_value:
            max_value = l[i]
    return max_value
