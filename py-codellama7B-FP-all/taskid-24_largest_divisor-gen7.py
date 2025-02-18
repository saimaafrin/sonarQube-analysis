def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    d = 1
    while d < n and n % d == 0:
        d += 1
    return d
