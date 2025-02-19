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

    for num1 in range(1, n // 4 + 1):
        for num2 in range(num1 + 1, n // 3 + 1):
            for num3 in range(num2 + 1, n // 2 + 1):
                if n == (num1 + num2 + num3) and num3 % 2 == 0:
                    return True
    return False
