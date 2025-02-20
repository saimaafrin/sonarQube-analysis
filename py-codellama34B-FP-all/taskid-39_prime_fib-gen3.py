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

    f1, f2 = 0, 1
    count = 0
    while True:
        f = f1 + f2
        f1, f2 = f2, f
        if f % 2 != 0 and is_prime(f):
            count += 1
        if count == n:
            return f
