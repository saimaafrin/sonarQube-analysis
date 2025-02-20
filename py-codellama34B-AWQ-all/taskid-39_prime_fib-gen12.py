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


    a, b, counter = 0, 1, 0

    while counter < n:
        a, b = b, a + b
        if is_prime(b) and b != 1:
            counter += 1
    return b
