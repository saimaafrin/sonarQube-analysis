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

    assert 0 <= n, "n must be positive or zero"
    assert p > 0, "p must be positive"

    power = 1
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = (result * power) % p
        power = (power * power) % p
        n = n // 2

    return result
