def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """


    for i in range(int(n**0.5), 0, -1):
        if n % i == 0:
            return i
    return 1
