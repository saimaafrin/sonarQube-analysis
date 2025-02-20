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

    def _fibfib(n: int) -> int:
        """A private function to compute the n-th element of the FibFib sequence.
        """
        if n <= 2:
            return n
        else:
            return _fibfib(n-1) + _fibfib(n-2) + _fibfib(n-3)
    return _fibfib(n)
