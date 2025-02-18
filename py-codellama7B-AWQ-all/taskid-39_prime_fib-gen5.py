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

    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
        if a % 2 == 0:
            a += 1
        if b % 2 == 0:
            b += 1
    return a if is_prime(a) else b
