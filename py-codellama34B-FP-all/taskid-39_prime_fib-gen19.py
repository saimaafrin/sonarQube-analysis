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


    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    prime_fib_list = []
    for i in range(1, n + 1):
        fib_n = fib(i)
        if is_prime(fib_n):
            prime_fib_list.append(fib_n)
    return prime_fib_list[-1]
