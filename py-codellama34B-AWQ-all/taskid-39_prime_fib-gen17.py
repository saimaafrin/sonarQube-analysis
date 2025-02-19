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

    n0, n1, i = 0, 1, 1
    while i < n:
        n2 = n0 + n1
        if is_prime(n2):
            i += 1
        n0, n1 = n1, n2
    return n2
