def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """


    # edge cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    # loop through all numbers smaller than n
    # if any number divides n evenly, return that number
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return i
