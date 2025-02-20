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

    if len(l) == 1:
        return True
    is_increasing = l[1] > l[0]
    for i in range(2, len(l)):
        if is_increasing and l[i] < l[i - 1]:
            return False
        if not is_increasing and l[i] > l[i - 1]:
            return False
    return True
