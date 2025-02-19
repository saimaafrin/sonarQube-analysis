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

    cache = {0: 0, 1: 0, 2: 1}

    def fibfib_helper(n: int) -> int:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibfib_helper(n-1) + fibfib_helper(n-2) + fibfib_helper(n-3)
            return cache[n]
    return fibfib_helper(n)
