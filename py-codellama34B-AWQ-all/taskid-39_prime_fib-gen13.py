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
        raise ValueError("n has to be positive integer")
    if n == 1:
        return 2
    fib_number = 2
    n -= 1
    fib_prime_number = 3
    n -= 1
    while n > 0:
        fib_number += fib_prime_number
        if is_prime(fib_number):
            fib_prime_number = fib_number
            n -= 1
    return fib_prime_number
