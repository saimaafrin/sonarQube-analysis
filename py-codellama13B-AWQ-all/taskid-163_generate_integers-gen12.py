from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    start = max(a, b)
    end = min(a, b)

    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)

    return result
