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
        raise ValueError("Input must be positive")
    if n == 1:
        return 2
    prev, curr = 1, 2
    while n > 1:
        while curr % 2 == 0 or curr % 5 == 0:
            curr += prev
        prev, curr = curr, curr + prev
        n -= 1
    return curr
