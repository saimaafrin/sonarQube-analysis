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

    # Initialize result
    result = []

    # Check if b is greater than a
    if b >= a:
        # Loop from a to b
        for num in range(a, b+1):
            # Check if the number is even
            if num % 2 == 0:
                # Add the number to the result
                result.append(num)
    else:
        # Loop from b to a
        for num in range(b, a+1):
            # Check if the number is even
            if num % 2 == 0:
                # Add the number to the result
                result.append(num)

    return result
