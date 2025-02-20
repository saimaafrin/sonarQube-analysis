from typing import List

def monotonic(l: List[int]) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if not len(l):
        return False
    # if the list has length 1 then there is nothing to check
    direction: int = l[1] - l[0]
    if direction == 0:
        return True

    for i in range(2, len(l)):
        new_direction = l[i] - l[i-1]
        if new_direction == 0:
            return True
        if direction != new_direction:
            return False
    return True
