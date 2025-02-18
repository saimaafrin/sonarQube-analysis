def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if str(i) + str(j) == "1" + str(n - 1):
                count += 1
            if str(n - 1) + str(j) == str(i) + "1":
                count += 1
    return count
