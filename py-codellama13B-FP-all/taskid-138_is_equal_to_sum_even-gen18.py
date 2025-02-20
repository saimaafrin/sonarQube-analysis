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

    # A number is the sum of exactly 4 positive even numbers if and only if its square is the sum of 4 consecutive even numbers
    if n % 4 == 1 or n % 4 == 2:
        return False
    square = n ** 2
    if square % 4 == 1 or square % 4 == 2:
        return False
    return True
