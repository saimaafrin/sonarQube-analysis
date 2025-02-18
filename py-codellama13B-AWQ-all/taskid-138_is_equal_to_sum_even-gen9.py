def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """

    if n < 4:
        return False

    # The number of positive even numbers n_1, n_2, n_3 and n_4
    # is determined by the fact that n = n_1 + n_2 + n_3 + n_4.
    # So n_1, n_2, n_3 and n_4 are positive integers such that
    # n_1 + n_2 + n_3 + n_4 = n
    # and n_1, n_2, n_3 and n_4 are all even.

    # Example
    # n = 8
    # n_1 = 2
    # n_2 = 2
    # n_3 = 2
    # n_4 = 2

    # n_1 = n - n_2 - n_3 - n_4
    # n_2 = n - n_1 - n_3 - n_4
    # n_3 = n - n_1 - n_2 - n_4
    # n_4 = n - n_1 - n_2 - n_3
    # => n_1 + n_2 + n_3 + n_4 = n
    # => n_1 = n/4

    # Now, we want to find n_1, n_2, n_3, n_4 so that n_1, n_2, n_3, n_4
    # are all positive integers and n_1, n_2, n_3, n_4 are all even.
    # We can find the greatest common divisor of n_1 and n_2 to
    # find the greatest common divisor of n_1, n_2, n_3, n_4.
    # Then, n_1 and n_2 are coprime integers so that n_1*n_2 is an even integer.
    # Also, n_1 and n_3 are coprime integers so that n_1*n_3 is an even integer.
    # Also, n_1 and n_4 are coprime integers so that n_1*n_4 is an even integer.
    # Thus, n_1, n_2, n_3 and n_4 are all even integers.

    n_1 = n // 4
    n_2 = n - n_1
    n_3 = n - n_1 - n_2
    n_4 = n - n_1 - n_2 - n_3

    return n_1 == n_2 and n_2 == n_3 and n_3 == n_4
