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
        raise ValueError(f"n must be >= 1, got {n}")

    fib = [0, 1]
    fib_prime = [0, 2]
    i = 1
    while len(fib_prime) < n:
        fib.append(fib[i] + fib[i - 1])
        if is_prime(fib[i]):
            fib_prime.append(fib[i])
        i += 1

    return fib_prime[n - 1]
