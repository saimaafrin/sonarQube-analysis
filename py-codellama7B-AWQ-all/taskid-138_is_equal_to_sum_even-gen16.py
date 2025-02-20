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

    if n % 2 != 0:
        return False

    num_of_even = 0
    while n > 0:
        if n % 2 == 0:
            num_of_even += 1
        n //= 2

    if num_of_even != 4:
        return False

    return True
