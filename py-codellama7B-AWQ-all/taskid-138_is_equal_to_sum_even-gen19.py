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

    for i in range(1, 10):
        if n == i * 4:
            return True
        if n == i * 5:
            return False
    return False
