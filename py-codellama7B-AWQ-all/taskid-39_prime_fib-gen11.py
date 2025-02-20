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

    if n < 1:
        raise ValueError('n must be > 0')

    # Fibonacci numbers: https://oeis.org/A000045
    # Fibonacci prime numbers: https://oeis.org/A000937

    fib_nums = [0, 1]
    i = 2
    while i < n:
        fib_nums.append(fib_nums[i - 1] + fib_nums[i])
        i += 1

    n_th_fib = fib_nums[n - 1]
    n_th_prime = next(filter(lambda x: is_prime(x), range(1, n_th_fib + 1)))
    return n_th_prime
