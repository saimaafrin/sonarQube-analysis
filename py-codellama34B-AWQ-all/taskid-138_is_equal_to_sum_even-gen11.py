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

    if n < 8:
        return False

    for i in range(4, n):
        count = 0
        for j in range(1, i):
            if i % 2 == 0:
                count += 1
            if count == 4:
                return True

    return False
