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
        raise ValueError("n should be a positive number")

    fib = 1
    prev_fib = 1
    count = 1

    while count < n:
        fib = fib + prev_fib
        if is_prime(fib):
            count += 1
        prev_fib = fib

    return fib
