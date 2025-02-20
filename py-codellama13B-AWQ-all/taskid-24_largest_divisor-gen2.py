def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    return next(divisor for divisor in range(n, 1, -1) if n % divisor == 0)
