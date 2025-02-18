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

    assert n > 0, "n must be greater than 0"

    fibs = [1, 2]
    i = 1

    while len(fibs) < n + 1:
        i += 1
        fibs.append(fibs[-1] + fibs[-2])

    primes = [2, 3, 5, 7, 11, 13]
    prime_fibs = []

    for f in fibs:
        if all(f % p != 0 for p in primes):
            prime_fibs.append(f)

    return prime_fibs[n - 1]
