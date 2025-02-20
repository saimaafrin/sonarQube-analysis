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

    i = 0
    a, b = 0, 1
    while i < n:
        a, b = b, a + b
        if isprime(b):
            i += 1
    return b
