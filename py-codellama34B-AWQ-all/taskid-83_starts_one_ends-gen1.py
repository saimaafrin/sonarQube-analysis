def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    n_digits = len(str(n))
    # count of numbers that end in 1
    numbers_that_end_in_1 = 10**(n_digits-1)
    # count of numbers that start in 1
    numbers_that_start_in_1 = 10**(n_digits-1) - 1

    return numbers_that_end_in_1 + numbers_that_start_in_1
