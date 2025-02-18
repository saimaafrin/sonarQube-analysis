def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1:
            count += 1
    return count
