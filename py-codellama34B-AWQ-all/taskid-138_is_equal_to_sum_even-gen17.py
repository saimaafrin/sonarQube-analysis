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

    assert n > 0
    for a in range(1, n):
        if n - a in range(2, n):
            for b in range(2, n - a):
                if n - a - b in range(2, n - a):
                    for c in range(2, n - a - b):
                        if n - a - b - c in range(2, n - a - b):
                            for d in range(2, n - a - b - c):
                                if (n - a - b - c - d) == 0:
                                    return True
    return False
