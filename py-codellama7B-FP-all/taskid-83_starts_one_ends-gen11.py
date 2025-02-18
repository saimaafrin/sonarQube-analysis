def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    n_digits = len(str(n))
    count = 0
    for i in range(n_digits):
        count += n_digits - i
    return count
