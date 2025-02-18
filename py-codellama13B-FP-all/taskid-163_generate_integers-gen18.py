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

    if a < 1 or b < 1:
        raise ValueError('Both a and b must be positive integers.')

    if a == b:
        return []

    numbers = []
    for i in range(min(a, b), max(a, b)):
        if str(i)[1] == '0':
            numbers.append(i)

    return sorted(numbers)
