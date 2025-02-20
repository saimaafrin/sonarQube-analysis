def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    for divisor in range(int(n / 2), 0, -1):
        if n % divisor == 0:
            return divisor
