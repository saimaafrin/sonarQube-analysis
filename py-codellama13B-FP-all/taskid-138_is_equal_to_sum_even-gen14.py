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

    if n < 0 or n % 2 == 1:
        return False

    count = 0
    n = int(n / 2)
    while n > 0:
        count += 1
        n -= 1

    return count == 4
