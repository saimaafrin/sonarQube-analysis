def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        i = 5
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return n
