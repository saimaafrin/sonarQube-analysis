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

    if n < 1:
        raise ValueError(f"{n} must be greater or equal than 1")

    i: int = 1
    prime_fib_number: int = 2
    a: int = 0
    b: int = 1
    c: int = a + b

    while i < n:
        a = b
        b = c
        c = a + b
        if c % 2 != 0 and c % 3 != 0 and c % 5 != 0 and c % 7 != 0:
            # number is prime
            i += 1
            prime_fib_number = c

    return prime_fib_number
