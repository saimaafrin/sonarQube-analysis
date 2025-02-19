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

    fib_list = [0, 1, 1]
    i = 2
    while True:
        fib_list.append(fib_list[i] + fib_list[i-1])
        if is_prime(fib_list[i+1]):
            i += 1
        if i == n:
            break
    return fib_list[n]
