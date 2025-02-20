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

    # n must be divisible by 2 to be sum of even numbers
    i = 0
    while i < (n / 2):
        i = i + 1
        j = 0
        while j < (n / 2):
            j = j + 1
            k = 0
            while k < (n / 2):
                k = k + 1
                if (i + j + k) == n:
                    return True
    return False
