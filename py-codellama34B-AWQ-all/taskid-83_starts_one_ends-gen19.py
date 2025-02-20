def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def num_start_with(num: int, digit: int) -> int:
        return num // 10 ** (num_digits(num) - digit)

    def num_end_with(num: int, digit: int) -> int:
        return num % 10 ** digit

    def num_digits(num: int) -> int:
        return len(str(num))

    count = 0

    for i in range(1, n + 1):
        count += (
            num_start_with(i, 1) == 1 or
            num_end_with(i, 1) == 1
        )

    return count
