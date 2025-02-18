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

    # https://oeis.org/A005765
    fibs = [1, 2, 3]
    i = 3
    while len(fibs) < n:
        i += 1
        fibs.append(fibs[i - 1] + fibs[i - 2])

    for f in fibs:
        if is_prime(f):
            n -= 1
            if n == 0:
                return f
