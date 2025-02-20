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

    # Check if n is a positive integer
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n must be a positive integer.")

    # Check if n is divisible by 4
    if n % 4 == 0:
        return True

    return False
