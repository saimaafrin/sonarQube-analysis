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

    # https://en.wikipedia.org/wiki/Fibonacci_number
    # fib(n) = fib(n-1) + fib(n-2)
    # fib(n) = fib(n-2) + fib(n-3) + fib(n-4)
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    while True:
        n += 1
        if is_prime(n) and n in fib:
            return n
