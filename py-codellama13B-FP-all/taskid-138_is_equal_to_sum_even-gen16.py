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

    # Check if n is even
    if n % 2 == 1:
        return False

    # Check if n is a perfect square
    sqrt_n = int(n**0.5)
    if sqrt_n**2 == n:
        return True

    # Check if n can be written as a sum of 4 even numbers
    i = 2
    while i < sqrt_n:
        j = sqrt_n - i
        if i * j == n:
            return True
        i += 1

    return False
