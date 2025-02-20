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

    # YOUR CODE HERE
    a, b = min(a, b), max(a, b)
    return [int(x) for x in str(b) if int(x) % 2 == 0 and a <= int(x) <= b]
