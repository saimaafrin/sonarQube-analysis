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

    i = 2
    n_even_sum = 0
    n_even_count = 0

    while n_even_count < 4:
        if i % 2 == 0 and n_even_sum + i <= n:
            n_even_sum += i
            n_even_count += 1
        i += 1

    return n_even_count == 4 and n_even_sum == n
