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

    fibs = []
    current = 0
    for _ in range(n + 1):
        current += 1
        fibs.append(current)
        for fib in fibs:
            if current % fib == 0:
                break
        else:
            return current
