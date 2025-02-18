def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    digits = list(map(int, str(n)))
    start = 1 in digits[:-1]
    end = 1 in digits[1:]
    return start + end
