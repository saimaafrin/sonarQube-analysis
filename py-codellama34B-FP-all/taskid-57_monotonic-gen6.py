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

    # First, check to see if there are any decreasing elements
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            # Decreasing elements found, so this is not a monotonic list
            return False

    # Second, check to see if there are any increasing elements
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            # Increasing elements found, so this is not a monotonic list
            return False

    # No decreasing or increasing elements found, so return True
    return True
