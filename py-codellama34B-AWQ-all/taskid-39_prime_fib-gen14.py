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
        raise ValueError("Expected a positive integer.")

    # The first two prime Fibonacci numbers are 2 and 3.
    if n == 1:
        return 2
    elif n == 2:
        return 3

    # Set up Fibonacci sequence.
    fib_prev = 1
    fib_curr = 2
    fib_next = 3
    prime_count = 2

    while True:
        # Check if the next Fibonacci number is prime.
        if is_prime(fib_next):
            prime_count += 1

        # If the number is prime, check if it's the n-th prime Fibonacci number.
        if prime_count == n:
            return fib_next

        # Calculate next Fibonacci number.
        fib_prev, fib_curr, fib_next = fib_curr, fib_next, fib_curr + fib_next
