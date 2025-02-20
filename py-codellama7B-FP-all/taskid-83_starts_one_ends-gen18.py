def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(10):
        if str(n)[0] == '1' or str(n)[-1] == '1':
            count += 1
    return count
