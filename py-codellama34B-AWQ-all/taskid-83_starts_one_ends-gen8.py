def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # find the count of n digit numbers
    count = 10 ** n - 10 ** (n - 1)
    # find the count of numbers that start with 1
    first_digit = count * 2
    # find the count of numbers that end with 1
    last_digit = count - first_digit
    return first_digit + last_digit
