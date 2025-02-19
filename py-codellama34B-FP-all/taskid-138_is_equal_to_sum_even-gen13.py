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

    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
            if count == 4:
                return True
            continue
        return False
