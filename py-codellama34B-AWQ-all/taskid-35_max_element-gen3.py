from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        return None
    max_el = l[0]
    for i in l:
        if i > max_el:
            max_el = i
    return max_el
