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

    prime_fibs = [2, 3, 5, 13]
    while len(prime_fibs) < n:
        last_prime_fib = prime_fibs[-1]
        next_prime_fib = last_prime_fib + 8 * last_prime_fib
        if next_prime_fib % 10 == 1:
            if is_prime(next_prime_fib):
                prime_fibs.append(next_prime_fib)
    return prime_fibs[n - 1]
