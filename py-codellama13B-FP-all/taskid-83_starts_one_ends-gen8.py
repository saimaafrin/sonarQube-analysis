def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    return len([i for i in range(10**n) if str(i)[:1] == '1' or str(i)[-1] == '1'])
