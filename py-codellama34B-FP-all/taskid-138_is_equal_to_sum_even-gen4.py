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

    for i in range(2, n + 1):
        for j in range(i + 2, n + 1):
            for k in range(j + 2, n + 1):
                l = n - i - j - k
                if l > 0 and i + j + k + l == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                    return True
    return False
