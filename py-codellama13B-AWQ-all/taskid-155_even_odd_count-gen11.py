from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """


    # Initialize the number of even and odd digits
    even_count = 0
    odd_count = 0

    # Iterate through the digits of the number
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
