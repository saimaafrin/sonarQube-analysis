def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def count_starting_ones(n: int) -> int:
        return 9 * 9 ** (n - 1)

    def count_ending_ones(n: int) -> int:
        return 9 * 9 ** (n - 1)

    return count_starting_ones(n) + count_ending_ones(n)
