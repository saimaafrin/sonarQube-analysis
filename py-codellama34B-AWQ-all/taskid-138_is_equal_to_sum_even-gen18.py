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

    a, b, c, d = 0, 0, 0, 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            a = i
            if (n - a) % 2 == 0:
                b = (n - a)
                for j in range(1, b + 1):
                    if j % 2 == 0:
                        c = j
                        if (b - c) % 2 == 0:
                            d = (b - c)
                            return True
    return False
