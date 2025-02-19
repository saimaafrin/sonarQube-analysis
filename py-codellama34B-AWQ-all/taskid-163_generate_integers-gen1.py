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

    # Initialize an empty list to store the even digits
    even_digits: List[int] = []

    # Iterate from a to b (or b to a)
    for num in range(a, b + 1):
        # Check if the number is even
        if num % 2 == 0:
            # If so, add it to the list
            even_digits.append(num)
    
    # Return the sorted list
    return sorted(even_digits)
