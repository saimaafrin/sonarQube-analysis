from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if len(l) == 0:
        raise ValueError("max_element is not defined for an empty list")
    else:
        max_val = l[0]
        for e in l[1:]:
            if e > max_val:
                max_val = e
        return max_val
