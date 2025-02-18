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


    def _is_even(n):
        return n % 2 == 0

    # check for invalid arguments
    if a < 1 or b < 1:
        return []

    # sort the arguments
    if a > b:
        a, b = b, a

    # get the numbers in between a and b that are even
    return list(filter(_is_even, range(a, b+1)))
