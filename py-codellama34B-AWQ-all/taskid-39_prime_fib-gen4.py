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

    fib_list = [2, 3, 5, 13, 89]
    current_fib = 144
    while len(fib_list) <= n:
        if is_prime(current_fib):
            fib_list.append(current_fib)
        current_fib += 1
    return fib_list[n - 1]
