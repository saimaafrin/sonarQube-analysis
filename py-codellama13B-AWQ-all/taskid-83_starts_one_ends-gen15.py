def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start = end = 0

    while n > 0:
        if n % 10 == 1:
            start += 1
        if n % 10 == 1 and n // 10 > 0:
            end += 1
        n //= 10

    return start + end
