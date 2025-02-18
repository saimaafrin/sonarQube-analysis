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


    # Check that a and b are positive integers
    if a < 1 or b < 1:
        raise ValueError("Both arguments must be positive integers.")

    # If a is greater than b, swap them
    if a > b:
        a, b = b, a

    # Initialise the list of integers
    integers = []

    # Loop through the range between a and b
    for i in range(a, b + 1):

        # If the current number is even, append it to the list
        if i % 2 == 0:
            integers.append(i)

    # Return the list of integers
    return integers
