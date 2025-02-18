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

    fib_1 = 0
    fib_2 = 1
    for _ in range(n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        if is_prime(fib_1):
            return fib_1
    raise ValueError("n should be a positive integer.")
