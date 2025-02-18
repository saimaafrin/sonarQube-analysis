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

    # If given number is even, it must be written as the sum of 4 even positive integers
    # If given number is odd, it can never be written as the sum of 4 even positive integers
    return (n & 1) == 0
