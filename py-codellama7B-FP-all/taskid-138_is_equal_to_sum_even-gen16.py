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

    if not isinstance(n, int):
        raise TypeError(f"The given n: {n} is not integer")
    if n <= 0:
        raise ValueError(f"The given n: {n} is not positive integer")
    if not n % 2 == 0:
        raise ValueError(f"The given n: {n} is not even number")

    for i in range(2, n, 2):
        if n - i in range(2, n, 2):
            return True
    return False
