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

    def is_even(n: int) -> bool:
        return n % 2 == 0

    def to_digits(n: int) -> List[int]:
        return [int(digit) for digit in str(n)]

    def get_even_digits(digits: List[int]) -> List[int]:
        return [digit for digit in digits if is_even(digit)]

    def compare(n: int, m: int) -> bool:
        return n < m

    def get_digits_between(n: int, m: int) -> List[int]:
        digits = []
        if compare(n, m):
            for i in range(n, m + 1):
                digits.extend(to_digits(i))
        else:
            for i in range(m, n + 1):
                digits.extend(to_digits(i))
        return get_even_digits(digits)

    if a > b:
        return get_digits_between(b, a)
    else:
        return get_digits_between(a, b)
