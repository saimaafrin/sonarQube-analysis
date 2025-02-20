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

    inc = dec = True
    for i in range(len(l) - 1):
        inc = inc and l[i] <= l[i+1]
        dec = dec and l[i] >= l[i+1]
    return inc or dec
