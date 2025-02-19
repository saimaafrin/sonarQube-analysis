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

    def is_even_digit(num: int) -> bool:
        """
        Returns true if the number has only even digits, false otherwise.
        """
        return all(int(digit) % 2 == 0 for digit in str(num))

    def digit_filter(num: int) -> bool:
        """
        Returns true if the number has any even digits, false otherwise.
        """
        return any(int(digit) % 2 == 0 for digit in str(num))

    if a >= b:
        return generate_integers(b, a)

    return sorted(filter(is_even_digit, range(a, b + 1)))
