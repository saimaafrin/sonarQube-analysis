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


    def fibfib_recursive(n: int) -> int:
        """
        >>> fibfib_recursive(1)
        0
        >>> fibfib_recursive(5)
        4
        >>> fibfib_recursive(8)
        24
        """
        if n < 3:
            return 0
        if n == 3:
            return 1
        return fibfib_recursive(n - 1) + fibfib_recursive(n - 2) + fibfib_recursive(n - 3)

    def fibfib_iterative(n: int) -> int:
        """
        >>> fibfib_iterative(1)
        0
        >>> fibfib_iterative(5)
        4
        >>> fibfib_iterative(8)
        24
        """
        fibfib_prev_prev = 0
        fibfib_prev = 0
        fibfib = 1
        for i in range(3, n + 1):
            fibfib_current = fibfib_prev + fibfib_prev_prev + fibfib
            fibfib_prev_prev = fibfib_prev
            fibfib_prev = fibfib
            fibfib = fibfib_current
        return fibfib

    return fibfib_iterative(n)
