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

    if n < 2:
        raise ValueError("n should be greater than 2")
    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return next((x for x in range(a, b + 1) if is_prime(x)), None)
