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
    for i in range(n):
        a, b = b, a + b
        if not a % 2 and a % 3:
            break
    else:
        raise ValueError(f"{n}th Fibonacci number is too big")
    return a
