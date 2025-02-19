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

    if n < 0:
        raise ValueError("n must be greater or equal to 0")
    if n < 3:
        return 0
    if n == 3:
        return 1
    else:
        fibfib_arr = [0] * (n + 1)
        fibfib_arr[0] = 0
        fibfib_arr[1] = 0
        fibfib_arr[2] = 1
        for i in range(3, n + 1):
            fibfib_arr[i] = fibfib_arr[i - 1] + fibfib_arr[i - 2] + fibfib_arr[i - 3]
        return fibfib_arr[n]
