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

    fib = [1, 2]
    i = 2
    while True:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
        if fib[-1] > n:
            break
    for j in range(2, n):
        if not is_prime(fib[j]):
            fib[j] = 0
    return fib.index(max(fib)) + 2
