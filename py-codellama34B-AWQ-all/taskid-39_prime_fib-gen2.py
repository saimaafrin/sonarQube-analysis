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

    f_1, f_2 = 0, 1
    count = 0
    while count < n:
        f_1, f_2 = f_2, f_1 + f_2
        if f_2 % 2 != 0 and is_prime(f_2):
            count += 1
    return f_2
