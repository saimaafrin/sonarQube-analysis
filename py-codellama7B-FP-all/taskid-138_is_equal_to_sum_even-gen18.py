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

    if n % 2 == 1:
        return False

    even_sum = 0
    for i in range(1, int(n/2) + 1):
        even_sum += i
        if even_sum == n:
            return True

    return False
