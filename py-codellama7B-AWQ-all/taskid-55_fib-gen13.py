def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # 0-th and 1-st Fibonacci numbers
    a, b = 0, 1
    # n-th Fibonacci number
    for i in range(n - 1):
        a, b = b, a + b
    return b
