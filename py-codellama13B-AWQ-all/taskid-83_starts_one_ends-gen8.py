def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start = int(str(n)[:1])
    end = int(str(n)[-1:])
    return start + end
