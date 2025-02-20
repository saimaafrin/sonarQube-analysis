def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a = 0
    b = 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    for i in range(n-2):
        a, b = b, a + b
    return b
