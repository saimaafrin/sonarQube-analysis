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

    # p must be odd
    assert p % 2 == 1, p

    if n == 0:
        return 1
    elif n % 2 == 0:
        result = modp(n//2, p) ** 2 % p
    else:
        result = modp(n-1, p) ** 2 % p

    return result
