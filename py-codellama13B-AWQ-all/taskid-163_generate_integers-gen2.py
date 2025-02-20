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

    # check if a is smaller than b
    if a > b:
        a, b = b, a

    # check if a is even
    if a % 2 != 0:
        a += 1

    # check if b is even
    if b % 2 != 0:
        b -= 1

    # check if the difference between a and b is odd
    if (b - a) % 2 != 0:
        b -= 1

    # create a list with the even numbers between a and b
    list_of_even_numbers = list(range(a, b + 1, 2))

    # return the list of even numbers between a and b
    return list_of_even_numbers
