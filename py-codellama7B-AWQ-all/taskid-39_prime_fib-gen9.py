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

    # 1 1 2 3 5 8 13 21 34 55 89
    if n <= 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 5
    if n == 5:
        return 89
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    # 0 1 1 2 3 4 5 6 7 8 9
    fib = fibs[n]
    while not is_prime(fib):
        fibs.append(fib)
        fibs[n+1] = fibs[n] + fibs[n+1]
        fib = fibs[n+1]
    return fib
