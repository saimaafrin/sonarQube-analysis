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

    # You may assume that a is less than or equal to b
    assert a <= b
    # You may assume that both a and b are positive
    assert a > 0 and b > 0

    return [i for i in range(a, b + 1) if i % 2 == 0]
