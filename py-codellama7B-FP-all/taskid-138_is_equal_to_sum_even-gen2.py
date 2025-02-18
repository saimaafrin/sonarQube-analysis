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

    even_sum = 0
    while n > 0:
        if n % 2 == 0:
            even_sum += n
            n -= 2
            if even_sum > 8:
                return False
        n -= 1
    return even_sum == 8
