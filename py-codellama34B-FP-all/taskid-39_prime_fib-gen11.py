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

    fibonacci = [0, 1]
    i = 1
    while True:
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
        i += 1
        if is_prime(fibonacci[i]) and i == n:
            return fibonacci[i]
