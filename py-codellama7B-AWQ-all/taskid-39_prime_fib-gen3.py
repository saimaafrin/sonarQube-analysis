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
        return -1
    elif n == 1:
        return 2

    i, j = 0, 1
    for _ in range(n):
        i, j = j, i + j
        if is_prime(i):
            return i

    return -1
