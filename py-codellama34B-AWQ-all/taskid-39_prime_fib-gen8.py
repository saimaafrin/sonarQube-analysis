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

    fibs = [0, 1, 1]
    index = 2
    while True:
        fibs.append(fibs[index] + fibs[index + 1])
        index += 1
        if is_prime(fibs[index]):
            n -= 1
        if n == 0:
            return fibs[index]
