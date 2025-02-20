def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Base case: 1 is the smallest number that divides every number
    if n > 1:
        for i in range(n, 1, -1):
            if n % i == 0:
                return i
