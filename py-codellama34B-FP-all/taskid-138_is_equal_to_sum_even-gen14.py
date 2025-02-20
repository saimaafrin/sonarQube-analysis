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

    if n < 8 or n % 2 != 0:
        return False
    for i in range(2, n):
        if (n - i) % 2 == 0:
            for j in range(2, i):
                if (n - i - j) % 2 == 0:
                    for k in range(2, j):
                        if n == i + j + k + (n - i - j):
                            return True
    return False
