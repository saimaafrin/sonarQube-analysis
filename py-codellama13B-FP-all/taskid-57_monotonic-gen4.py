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


    # If the list has less than 2 elements, it's monotonic.
    if len(l) < 2:
        return True

    # If the list has 2 or more elements, it's monotonic if the first and
    # last elements are the same, or if the first element is less than or
    # equal to the second element and all subsequent elements are less
    # than or equal to the previous element.
    if l[0] <= l[-1]:
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                return False
        return True
    else:
        for i in range(1, len(l)):
            if l[i] > l[i-1]:
                return False
        return True
