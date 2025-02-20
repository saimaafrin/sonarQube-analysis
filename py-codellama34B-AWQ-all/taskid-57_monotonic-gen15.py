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

    direction: int = 0
    for i in range(len(l) - 1):
        if l[i + 1] > l[i]:
            direction += 1
        elif l[i + 1] < l[i]:
            direction -= 1
        else:
            direction = 0
        if direction != 0 and direction != -1 and direction != 1:
            return False
    return True
