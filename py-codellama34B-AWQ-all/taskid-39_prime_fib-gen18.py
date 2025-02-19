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

    if n <= 1:
        return 2
    first, second, current = 1, 1, 2
    count = 2
    while count < n:
        current = first + second
        if current % 2 != 0:
            count += 1
        first = second
        second = current
    return current
