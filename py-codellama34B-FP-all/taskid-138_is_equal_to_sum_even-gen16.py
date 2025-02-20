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

    count_even = 0
    count_even_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count_even += 1
            count_even_sum += i
        if count_even == 4 and count_even_sum == n:
            return True
        if count_even == 4 and count_even_sum != n:
            return False
    return False
