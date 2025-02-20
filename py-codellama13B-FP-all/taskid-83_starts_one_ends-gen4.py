def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    num = int(str(n) * 2)
    return int(str(num).count(str(n)))
