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

    if a == b:
        return []

    # Ensure that 'a' is the smaller of the two numbers
    if b < a:
        a, b = b, a

    # Get all the even numbers between a and b
    nums = [num for num in range(a, b + 1) if num % 2 == 0]

    return nums
