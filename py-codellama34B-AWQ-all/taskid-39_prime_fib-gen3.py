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

    i = 0
    j = 1
    k = 1
    prime_found = False
    while not prime_found:
        k = i + j
        i = j
        j = k
        if is_prime(k):
            n -= 1
            if n == 0:
                prime_found = True
    return k
