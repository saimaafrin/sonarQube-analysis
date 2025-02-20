def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count_start = 0
    count_end = 0
    for i in range(10 ** (n - 1)):
        if i == 0 or i == 9:
            count_start += 1
        elif i == 1:
            count_start += 1
            count_end += 1
        elif i == 8:
            count_end += 1
        else:
            count_start += 1
            count_end += 1
    return count_start + count_end
