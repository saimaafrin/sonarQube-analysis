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

    a = 1
    b = 2
    c = 0
    i = 2

    while i <= n:
        c = a + b
        a = b
        b = c
        if is_prime(c):
            i += 1

    return c
