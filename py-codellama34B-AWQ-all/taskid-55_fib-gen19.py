def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    if n < 1:
        raise ValueError("n must be >= 1")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
