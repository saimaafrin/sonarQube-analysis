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
    if p == 1:
        return 0

    # p is odd
    if p & 1 == 1:
        # n odd
        if n & 1 == 1:
            return (modp(n >> 1, p) ** 2) % p
        # n even
        return (modp(n >> 1, p)) ** 2 % p

    # p is even
    if n & 1 == 1:
        return (modp(n >> 1, p) ** 2) % p
    return (modp(n >> 1, p)) ** 2 % p
