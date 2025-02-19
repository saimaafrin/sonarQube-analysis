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

    res: List[int] = []
    if a > b:
        b, a = a, b
    for i in range(a, b+1):
        n = str(i)
        if len(n) != len(str(b)):
            continue
        for j in n:
            if int(j) % 2 == 0:
                res.append(int(j))
    return sorted(res)
