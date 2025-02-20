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

    fib_list = [0, 1]
    prime_list = [2]
    # generate Fibonacci number until n-th number
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    # check if fib_list[n-1] is prime
    for i in range(2, int(sqrt(fib_list[n - 1]) + 1)):
        if fib_list[n - 1] % i == 0:
            break
    else:
        # fib_list[n-1] is prime
        prime_list.append(fib_list[n - 1])

    # check if fib_list[n-2] is prime
    for i in range(2, int(sqrt(fib_list[n - 2]) + 1)):
        if fib_list[n - 2] % i == 0:
            break
    else:
        # fib_list[n-2] is prime
        prime_list.append(fib_list[n - 2])

    return prime_list[-1]
