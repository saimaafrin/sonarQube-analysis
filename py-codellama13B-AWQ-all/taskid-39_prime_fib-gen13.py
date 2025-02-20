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

    fib_seq = []
    fib_seq.append(1)
    fib_seq.append(1)
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])
    for i, num in enumerate(fib_seq):
        if is_prime(num) and i == n - 1:
            return num
        else:
            continue
