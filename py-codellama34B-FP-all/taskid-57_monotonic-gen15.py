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

    # Check if first number is smaller than last number
    if l[0] < l[-1]:
        # If so, check if all numbers are monotonically increasing
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    else:
        # If not, check if all numbers are monotonically decreasing
        return all(l[i] >= l[i + 1] for i in range(len(l) - 1))
