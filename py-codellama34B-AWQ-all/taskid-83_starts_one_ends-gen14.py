def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    num_digits = len(str(n))
    return 2 * (10 ** (num_digits - 1))
