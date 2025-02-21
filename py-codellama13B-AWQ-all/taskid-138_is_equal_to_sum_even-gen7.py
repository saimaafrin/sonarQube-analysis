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
    if n % 2 == 1:
        return False
    if n == 4:
        return True
    for i in range(2, n // 2):
        if i * i == n:
            return True
    return False
