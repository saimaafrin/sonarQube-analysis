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

    # This is the way I'd write it, in one line:
    # fibfib = lambda n: 0 if n <= 1 else (n if n <= 3 else fibfib(n-1) + fibfib(n-2) + fibfib(n-3))
    # return fibfib(n)

    # This is a more verbose, but more readable version of the function:
    if n <= 1:
        return 0
    elif n <= 3:
        return n
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
