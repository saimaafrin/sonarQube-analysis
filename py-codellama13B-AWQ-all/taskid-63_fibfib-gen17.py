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

    if n < 3:
        return n
    fibfib_prev = 0
    fibfib_prev2 = 1
    fibfib_prev3 = 0
    for _ in range(n - 2):
        fibfib_next = fibfib_prev + fibfib_prev2 + fibfib_prev3
        fibfib_prev3 = fibfib_prev2
        fibfib_prev2 = fibfib_prev
        fibfib_prev = fibfib_next
    return fibfib_prev
