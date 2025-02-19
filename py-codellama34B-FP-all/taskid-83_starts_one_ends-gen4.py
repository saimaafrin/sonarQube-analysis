def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    total = 0
    for i in range(n, 10**(n-1), 10):
        total += i + i-10**(n-1)
    return total + (2*10**(n-1) - 10**(n-1))
