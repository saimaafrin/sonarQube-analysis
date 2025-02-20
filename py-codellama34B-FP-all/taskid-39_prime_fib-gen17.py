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


    phi = (1 + 5 ** 0.5) / 2

    a = round(phi ** n / 5 ** 0.5)

    b = round((1 - phi) ** (-n) * (1 + 5 ** 0.5))

    return int((a - b) / 2)
