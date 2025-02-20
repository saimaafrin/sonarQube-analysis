from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Your code here
    if not l:
        return None
    max_number = l[0]
    for i in l[1:]:
        if i > max_number:
            max_number = i
    return max_number
