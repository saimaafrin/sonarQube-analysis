def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2

    # Find the number of integers that start with 1
    count = 10 ** (n - 1)

    # Find the number of integers that end with 1
    if n % 2 == 1:
        # If n is odd, there will be n // 2 numbers that end with 1
        count += n // 2
    else:
        # If n is even, there will be n // 2 numbers that end with 1
        count += n // 2 - 1

    return count
