def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    i = 1
    while i < n:
        if n % i == 0:
            return i
        else:
            i += 1
    raise ValueError("Input number should be larger than 1")
