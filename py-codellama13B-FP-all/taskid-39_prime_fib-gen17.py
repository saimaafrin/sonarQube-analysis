def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    if n < 1:
        raise ValueError("n must be greater or equal than 1")
    a, b = 0, 1
    c = a + b
    while n > 0:
        if is_prime(c):
            n -= 1
        a, b = b, c
        c = a + b
    return c
