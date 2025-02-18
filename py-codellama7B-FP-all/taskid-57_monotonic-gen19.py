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

    # check if list is not empty
    if len(l) <= 1:
        return True
    # check if list is decreasing
    if l[0] > l[-1]:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
        return True
    # check if list is increasing
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True
