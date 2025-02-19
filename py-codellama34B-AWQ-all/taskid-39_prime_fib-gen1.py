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

    if n <= 1:
        return 2
    else:
        prime = 0
        fib = 0
        count = 0
        while count < n:
            fib += prime
            prime = fib - prime
            if is_prime(fib):
                count += 1

        return fib
