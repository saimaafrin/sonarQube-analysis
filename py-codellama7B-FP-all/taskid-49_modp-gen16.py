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
    elif p == 1:
        return 0
    else:
        n1 = modp(n - 1, p)
        n1 *= 2
        return n1 % p
