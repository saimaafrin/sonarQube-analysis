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

    num_list = [0, 0, 0, 0]
    if n % 2 != 0:
        return False
    for i in range(4):
        if n == 0:
            return False
        for j in range(1, n + 1):
            if n == 0:
                return False
            if j % 2 == 0 and n - j >= 0:
                num_list[i] = j
                n -= j
                break
    if sum(num_list) == n:
        return True
    return False
