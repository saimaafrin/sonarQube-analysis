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

    if n % 2 != 0:
        return False

    for i in range(2, int(n / 4) + 1):
        if n == (2 * i) + (2 * (i - 1)) + (2 * (i - 2)) + (2 * (i - 3)):
            return True
    return False
