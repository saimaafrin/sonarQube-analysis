def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """


    # Fibonacci sequence:
    # fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, fib(5) = 5, fib(6) = 8, fib(7) = 13, fib(8) = 21, fib(9) = 34
    # FibFib sequence:
    # fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1, fibfib(3) = 2, fibfib(4) = 4, fibfib(5) = 8, fibfib(6) = 15, fibfib(7) = 24, fibfib(8) = 39, fibfib(9) = 64
    # fibfib(n) = fib(n-1) + fib(n-2) + fib(n-3)

    def fib(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2) + fib(n - 3)

    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fib(n)
