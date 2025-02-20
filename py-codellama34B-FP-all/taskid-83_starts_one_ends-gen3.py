def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    n_digits = [10 ** (i - 1) for i in range(1, 10)]
    count = 0
    for n_digit in n_digits:
        if n_digit <= n:
            count += 2 * n_digit
        else:
            break
    return count + (n - sum(n_digits))
