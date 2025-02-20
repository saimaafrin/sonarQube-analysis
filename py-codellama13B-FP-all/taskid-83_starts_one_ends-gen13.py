def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # check input
    if n < 1:
        raise ValueError("n must be greater than 0")

    count = 0
    for start in range(1, 10):
        for end in range(1, 10):
            count += 1 if start == end else 0

    return count
