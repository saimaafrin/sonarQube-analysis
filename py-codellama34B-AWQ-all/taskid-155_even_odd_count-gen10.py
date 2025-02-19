from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    count_odd = 0
    count_even = 0
    # loop through the number and find the count of even and odd digits
    for n in list(str(num)):
        if int(n) % 2:
            count_odd += 1
        else:
            count_even += 1
    return count_even, count_odd
