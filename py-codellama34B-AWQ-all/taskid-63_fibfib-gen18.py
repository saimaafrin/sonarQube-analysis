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


    if n == 0:
        return 0
    if n <= 3:
        return 1

    fib_0, fib_1, fib_2 = 0, 0, 1
    for i in range(3, n + 1):
        fib = fib_0 + fib_1 + fib_2
        fib_0, fib_1, fib_2 = fib_1, fib_2, fib

    return fib
