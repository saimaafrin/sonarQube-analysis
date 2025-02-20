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

    if n <= 0:
        raise ValueError("n must be greater than 0")
    current = 2
    current_index = 1
    next_ = 3
    while current_index < n:
        current, next_ = next_, current + next_
        if next_ % 2 != 0:
            current_index += 1
    return current
