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

    if n <= 0:
        raise ValueError("n has to be positive")
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if a > b:
            break
        if a % 2 == 0 and a != 2:
            continue
        if is_prime(a):
            count += 1
            if count == n:
                return a
