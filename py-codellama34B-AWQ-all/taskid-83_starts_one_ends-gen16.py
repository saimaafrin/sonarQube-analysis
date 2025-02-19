def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 1. First digit
    num_of_first = n
    # 2. Last digit
    num_of_last = n
    # 3. Sum
    return num_of_first + num_of_last
