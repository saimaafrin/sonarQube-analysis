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

    n = n - 1
    fib = 0
    fib_n = 0
    while not fib_is_prime(fib):
        fib_n += 1
        fib = fib_n
    return fib
