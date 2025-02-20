def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 1. Counting 1-digit numbers
    num_digits = len(str(n))
    num_digits_1 = n // 10**(num_digits - 1)
    count = num_digits_1

    # 2. Counting other numbers
    for num_digits in range(2, num_digits+1):
        # A. Start with 1
        count += 9 * (10**(num_digits-1) - 10**(num_digits-2))

        # B. End with 1
        count += 9 * (10**(num_digits-1) - 10**(num_digits-2))

    return count
