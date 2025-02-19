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

    count = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            continue
        for j in range(i + 1, n + 1):
            if j % 2 == 1:
                continue
            for k in range(j + 1, n + 1):
                if k % 2 == 1:
                    continue
                for m in range(k + 1, n + 1):
                    if m % 2 == 1:
                        continue
                    if i + j + k + m == n:
                        count += 1
    return count == 1
