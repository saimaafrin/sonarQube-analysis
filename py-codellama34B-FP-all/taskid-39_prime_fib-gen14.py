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


    # Fibonacci series up to nth term
    fibonacci_seq = [0, 1]
    while True:
        fibonacci_seq.append(fibonacci_seq[-2] + fibonacci_seq[-1])
        if len(fibonacci_seq) > n:
            fibonacci_seq.pop()
            break

    # check if the numbers are prime
    prime_numbers = [num for num in fibonacci_seq if is_prime(num)]

    # return nth prime fibonacci number
    return prime_numbers[n - 1]
