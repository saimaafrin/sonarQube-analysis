def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Edge cases
    if n < 1:
        raise ValueError('n must be greater than 0')
    if n > 10:
        raise ValueError('n must be less than 10')

    # Base case
    if n == 1:
        return 1

    # Recursive case
    return (10 ** (n - 1)) + (10 ** n) - 1
