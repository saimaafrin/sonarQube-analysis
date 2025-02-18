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

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # find the first number greater than 2
        # that is also prime and a Fibonacci number
        i = 5
        while not is_prime(i) or not is_fibonacci(i):
            i += 1
        return i
