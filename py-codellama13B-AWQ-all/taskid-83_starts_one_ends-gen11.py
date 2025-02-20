def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # For example, when n=2, there are 11 numbers that start or end with 1
    # that are 2 digits long: 10, 11, 19, 12, 13, 14, 15, 16, 17, 18, 19
    count = 0
    for i in range(10 ** (n - 1)):
        if i % 10 == 0:
            count += 1
        if i // 10 == 10:
            count += 1
    return count
