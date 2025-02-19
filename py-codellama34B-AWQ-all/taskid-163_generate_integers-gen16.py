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

    if a > b:
        a, b = b, a
    ret = []
    for n in range(a, b + 1):
        for d in str(n):
            if int(d) % 2 == 0:
                ret.append(int(d))
    return sorted(set(ret))
