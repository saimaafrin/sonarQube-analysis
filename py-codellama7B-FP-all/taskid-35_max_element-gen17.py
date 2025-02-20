from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # if l is empty then return maximum value
    if not l:
        return None
    # set maximum element to the first element of list
    maximum = l[0]
    for element in l:
        if element > maximum:
            maximum = element
    return maximum
