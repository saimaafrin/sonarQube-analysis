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

    fib = [0, 1]
    i = 2
    while i <= n:
        fib.append(fib[-1] + fib[-2])
        i += 1
    for i in range(2, len(fib)):
        if is_prime(fib[i]):
            return fib[i]
    raise Exception(f"No prime fibonacci number for n={n}")
