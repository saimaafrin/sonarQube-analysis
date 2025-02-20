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


    def is_even(n):
        return n % 2 == 0

    numbers = range(1, 10)
    if sum(filter(is_even, numbers)) == n:
        return True
    return False
