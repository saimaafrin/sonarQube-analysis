def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2
    first_digit = 10**(n-1)
    last_digit = 10**(n-1) - 1
    return 2 * last_digit + first_digit + 1
