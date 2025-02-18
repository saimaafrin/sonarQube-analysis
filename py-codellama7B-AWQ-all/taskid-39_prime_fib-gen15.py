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

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 1, 2
        for i in range(n - 2):
            a, b = b, a + b
            if is_prime(a):
                n -= 1
                if n == 0:
                    return a
    return -1
