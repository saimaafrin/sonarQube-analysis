def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Get number of digits.
    digits = len(str(n))
    return pow(10, digits-1) + pow(10, digits-2)
