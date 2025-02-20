def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def num_digits(n: int) -> int:
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        return count

    n_digits = num_digits(n)
    if n_digits == 1:
        return 1

    start_end = 0
    for i in range(1, 10):
        start_end += pow(10, n_digits - 1) * (9 - i)
        start_end += pow(10, n_digits - 2) * (9 - i)

    return start_end
