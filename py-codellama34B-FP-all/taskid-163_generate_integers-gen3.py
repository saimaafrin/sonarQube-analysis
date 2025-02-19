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
        return generate_integers(b, a)

    numbers: List[int] = []
    for number in range(a, b + 1):
        for digit in str(number):
            if int(digit) % 2 == 0:
                numbers.append(int(digit))
    return list(set(numbers))
