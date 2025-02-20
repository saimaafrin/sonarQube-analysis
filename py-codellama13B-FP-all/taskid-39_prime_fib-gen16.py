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

    if n == 0:
        return 0
    if n == 1:
        return 2
    i = 2
    while True:
        num = fibonacci_number(i)
        if is_prime(num) and num % 4 == 1:
            if n == i:
                return num
            i += 1
        else:
            i += 1
