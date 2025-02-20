def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n == 0 or n == 1:
        return n
    for i in range(n, 1, -1):
        if n % i == 0:
            return i
