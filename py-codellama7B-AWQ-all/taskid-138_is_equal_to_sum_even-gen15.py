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

    if n % 2 == 1:
        return False
    a, b, c, d = 2, 3, 4, 5
    while True:
        e = a + b + c + d
        if e == n:
            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
                return True
        a += 1
        b += 1
        c += 1
        d += 1
