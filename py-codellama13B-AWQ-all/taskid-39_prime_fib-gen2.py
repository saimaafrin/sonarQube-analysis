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


    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return -1

    return a
