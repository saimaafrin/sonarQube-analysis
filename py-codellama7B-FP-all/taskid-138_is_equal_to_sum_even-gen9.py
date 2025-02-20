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

    even_numbers = [2, 4, 6, 8]
    for even_num in even_numbers:
        if even_num == n:
            return False
        elif even_num > n:
            return False
        else:
            n -= even_num
    return n == 0
