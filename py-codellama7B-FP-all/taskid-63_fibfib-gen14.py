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

    if n < 3:
        return 1

    previous_value = 1
    previous_previous_value = 0
    for i in range(n - 2):
        current_value = previous_value + previous_previous_value
        previous_previous_value = previous_value
        previous_value = current_value

    return previous_value
