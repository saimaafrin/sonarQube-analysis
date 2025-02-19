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

    if not is_multiple_of_4(n):
        return False

    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    if i + j + k + l == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                        a = i
                        b = j
                        c = k
                        d = l
                        return True

    return False
