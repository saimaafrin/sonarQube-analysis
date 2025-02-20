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

    if n <= 2:
        return 0 if n == 2 else 0
    cache = {}
    cache[0] = 0
    cache[1] = 0
    cache[2] = 1
    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[n]
