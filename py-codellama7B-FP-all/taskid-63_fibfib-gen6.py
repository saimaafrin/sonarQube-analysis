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

    def fibfib_n(n: int) -> int:
        if n < 3:
            return 0
        # fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        #           == fibfib(n-2) + fibfib(n-3) + fibfib(n-4)
        #           == fibfib(n-3) + fibfib(n-4) + fibfib(n-5)
        #           == ...
        #           == fibfib(n-n+2) + fibfib(n-n+3) + fibfib(n-n+4)
        #           == fibfib(n-n+1) + fibfib(n-n+2)
        return fibfib_n(n-1) + fibfib_n(n-2)
    return fibfib_n(n)
