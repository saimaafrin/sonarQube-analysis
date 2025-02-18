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
    sum_of_even_numbers = sum(even_numbers)
    if n == sum_of_even_numbers:
        return True
    else:
        return False
