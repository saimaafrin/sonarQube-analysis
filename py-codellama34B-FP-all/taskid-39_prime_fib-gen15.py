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

    fib = [1, 1]
    if n <= 2:
        return fib[n - 1]

    while True:
        next_fib = fib[-2] + fib[-1]
        if next_fib > fib[-1]:
            fib.append(next_fib)
            if is_prime(next_fib):
                n -= 1
                if n == 0:
                    return next_fib
        else:
            return None
