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

    fib_seq = [1, 1, 2, 3, 5]
    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])

    for i in range(2, int(n**0.5) + 1):
        if fib_seq[n] % i == 0:
            fib_seq[n] += 1

    while not is_prime(fib_seq[n]):
        fib_seq[n] += 1

    return fib_seq[n]
