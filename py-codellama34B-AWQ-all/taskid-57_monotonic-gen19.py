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


    if len(l) <= 1:
        return True

    is_increasing = l[0] <= l[1]

    for i in range(2, len(l)):
        if is_increasing:
            if l[i - 1] > l[i]:
                return False
        else:
            if l[i - 1] < l[i]:
                return False

    return True
