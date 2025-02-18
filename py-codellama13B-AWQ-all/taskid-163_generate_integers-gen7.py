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


    if a >= b:
        return []

    if a < 0:
        a = 0

    if b < 0:
        b = 0

    if b > 9:
        b = 9

    if a % 2 == 1:
        a += 1

    output = []

    for num in range(a, b + 1):
        if num % 2 == 0:
            output.append(num)

    return output
