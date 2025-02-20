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

    # Fibonacci sequence
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b

    # check prime
    if is_prime(a):
        return a
    else:
        return prime_fib(n + 1)
