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


    # check for positive number
    if n <= 0:
        return False

    # check for even number
    if n % 2 != 0:
        return False

    # evaluate for sum of even numbers
    for i in range(1, n):
        if i % 2 == 0:
            if n - i % 2 == 0:
                return True

    return False
