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

    assert n >= 10
    for i in range(2, 9):
        for j in range(2, 9):
            for k in range(2, 9):
                for l in range(2, 9):
                    if i != j != k != l:
                        if i + j + k + l == n:
                            return True
    return False
