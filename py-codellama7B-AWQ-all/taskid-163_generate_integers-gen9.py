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


    # If a and b are equal, return an empty list.
    if a == b:
        return []

    # If a is greater than b, swap them.
    if a > b:
        a, b = b, a

    # Create a list to hold the result.
    result = []

    # Iterate from a to b, adding each even number to the result.
    for x in range(a, b + 1):
        if x % 2 == 0:
            result.append(x)

    # Return the result.
    return result
