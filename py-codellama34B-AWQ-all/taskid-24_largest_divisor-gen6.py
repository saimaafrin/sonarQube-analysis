def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # this is a very naive implementation of the Euclidean algorithm
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return 1
