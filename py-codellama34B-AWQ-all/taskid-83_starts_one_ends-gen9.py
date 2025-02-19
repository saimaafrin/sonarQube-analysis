def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def count_digits(n: int, one_digit: int, num: int) -> int:
        if n == 1:
            if num == one_digit:
                return 1
            return 0
        return count_digits(n-1, one_digit, num) + count_digits(n-1, one_digit, num*10 + one_digit)

    return count_digits(n, 1, 1) + count_digits(n, 1, 10)
