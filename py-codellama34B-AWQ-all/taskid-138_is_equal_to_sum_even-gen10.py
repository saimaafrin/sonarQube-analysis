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

    ctr = 0
    if n % 2 == 1:
        return False
    for i in range(2, n // 2):
        for j in range(i, n // 2):
            for k in range(j, n // 2):
                for l in range(k, n // 2):
                    if i + j + k + l == n:
                        ctr += 1
                        return ctr == 1
    return False
