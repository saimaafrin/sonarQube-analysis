def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    divisors.sort()
    return divisors[-1]
