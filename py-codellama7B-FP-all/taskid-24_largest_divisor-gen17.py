def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        largest = 2
    else:
        largest = 1

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            largest = i

    return largest
