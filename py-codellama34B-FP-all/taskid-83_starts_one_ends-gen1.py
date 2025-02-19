def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    prefix = "1"
    suffix = "1"

    for _ in range(n - 2):
        prefix += "0"
        suffix = "0" + suffix

    return int(suffix) + len(prefix) * 9 * 10 ** (n - 2)
