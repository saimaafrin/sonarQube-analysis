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
        if a % 2 == 0:
            return [a]
        return []

    if a > b:
        (a, b) = (b, a)

    # We can calculate the number of even numbers in a and b:
    #   10^n - 10^n % 2
    #   e.g. 10^2 - 10^2 % 2 = 100 - 0 = 100
    #   e.g. 10^3 - 10^3 % 2 = 1000 - 888 = 112
    #
    # We can use this to get the number of even numbers in the range:
    #   (10^n - 10^n % 2) - (10^(n-1) - 10^(n-1) % 2)
    #   e.g. (10^2 - 10^2 % 2) - (10^1 - 10^1 % 2) = 100 - 0 - 10 = 90
    #   e.g. (10^3 - 10^3 % 2) - (10^2 - 10^2 % 2) = 112 - 100 = 12
    #
    # We can then generate the range, and filter out any odd numbers
    #   e.g. range(100, 100 + 12) = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
    #   e.g. range(100, 100 + 12) = [100, 102, 104, 106, 108, 110]

    num_digits = len(str(a))
    max_number = 10 ** num_digits
    even_numbers = [i for i in range(max_number - max_number % 2, max_number)]
    return [n for n in even_numbers if n % 2 == 0 and n >= a and n <= b]
