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

    if n % 2 != 0:
        return False
    else:
        sum_of_even_numbers = 0
        for i in range(4):
            sum_of_even_numbers += (n - i) // (i + 1)
        return n == sum_of_even_numbers
