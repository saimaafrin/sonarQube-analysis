def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def _count_numbers(n: int, prefix: str) -> int:
        """
        Count numbers with given prefix.
        """
        if n == 1:
            return 1
        # prefix = '1' * len(prefix)
        return 10 ** (n - len(prefix)) * len(prefix)

    return _count_numbers(n, '1') - 1
