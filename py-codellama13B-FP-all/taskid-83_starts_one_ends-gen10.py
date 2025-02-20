def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # We only need to consider numbers from 1 to 9 because the maximum
    # number of leading or trailing 1's is 9 (111111111).
    count = 0
    for i in range(1, 10):
        # A number starts with 1 has 9 possibilities of the last digit.
        # E.g. 111111111 (9 possibilities)
        count += 9
        # A number ends with 1 has 9 possibilities of the first digit.
        # E.g. 111111111 (9 possibilities)
        count += 9
    # A number starts and ends with 1 has 9 possibilities of the middle
    # digits. E.g. 111111111 (9 possibilities)
    count += 9
    return count
