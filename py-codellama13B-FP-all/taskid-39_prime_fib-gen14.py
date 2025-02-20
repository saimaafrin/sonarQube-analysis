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

    # Fibonacci numbers
    fibs = [0, 1, 1]
    for i in range(3, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    # Prime numbers
    primes = [2]
    for i in range(3, 10000):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # Find
    prime_fib = 0
    for i in range(n):
        if primes[i] in fibs:
            prime_fib = primes[i]
            break

    return prime_fib
