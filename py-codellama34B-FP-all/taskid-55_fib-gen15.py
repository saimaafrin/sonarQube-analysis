def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a, b = 0, 1
    while n > 0:
        if n % 2 == 1:
            a, b = b, a + b
        n //= 2
    return a
