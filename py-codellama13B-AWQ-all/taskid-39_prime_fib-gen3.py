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
        raise ValueError('n must be greater than 0')

    def get_fib_prime(n: int, p: int, q: int) -> int:
        while True:
            p += q
            q += p
            if is_prime(p) and is_fib(p):
                if n == 1:
                    return p
                n -= 1

    return get_fib_prime(n, 0, 1)
