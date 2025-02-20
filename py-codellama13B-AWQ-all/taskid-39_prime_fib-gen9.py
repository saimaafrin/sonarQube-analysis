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

    if n <= 0:
        raise ValueError(f'n must be greater than 0.')

    # a, b = 0, 1
    # c = a + b
    # while c < n:
    #     a, b = b, c
    #     c = a + b
    # return c

    nth_fib = 0
    a, b = 0, 1
    while nth_fib < n:
        a, b = b, a + b
        nth_fib += 1

    while not is_prime(b):
        a, b = b, a + b
        nth_fib += 1
    return b
