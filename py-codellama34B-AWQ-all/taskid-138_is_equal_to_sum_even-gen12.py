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

    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(2, n + 1):
        a = i
        for j in range(2, n + 1 - i):
            b = j
            for k in range(2, n + 1 - i - j):
                c = k
                d = n - a - b - c
                if (a * a + b * b + c * c == d * d) and (a != b != c != d) and a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
                    return True
    return False
