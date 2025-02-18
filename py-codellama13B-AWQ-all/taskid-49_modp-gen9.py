def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """

    if n == 0:
        return 1
    if n < 0:
        raise ValueError(f"n must be positive: {n}")
    if p < 2 or p > 10000000:
        raise ValueError(f"p must be between 2 and 10000000: {p}")
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * p % 10000000
        p = p * p % 10000000
        n = n // 2
    return result
