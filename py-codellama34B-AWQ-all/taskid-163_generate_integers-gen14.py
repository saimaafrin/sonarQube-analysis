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

    # Initialize the empty list that will store the even digits between a and b
    even_digits = []

    # Check if a and b are both positive integers
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
        # If a is greater than b, we swap a and b
        if a > b:
            a, b = b, a

        # Loop through all the integers between a and b
        for i in range(a, b + 1):
            # If the integer is even and has at least one even digit,
            # we add it to the even_digits list
            if i % 2 == 0 and len(str(i)) > 1:
                even_digits.append(i)

    # Return the sorted even_digits list
    return sorted(even_digits)
