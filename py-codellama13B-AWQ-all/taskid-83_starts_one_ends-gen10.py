def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, 10):
        count += 1 if str(i) in str(n) else 0
        count += 1 if str(n)[0] == "1" else 0
    return count
