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


    if n < 2 or n % 2 != 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if i % 2 == 0:
            if n - i in [2, 4, 6, 8]:
                return True
    return False
