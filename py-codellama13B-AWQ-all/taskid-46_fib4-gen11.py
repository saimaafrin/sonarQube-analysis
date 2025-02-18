def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # This problem could be solved by a lot of different ways,
    # but a dynamic programming approach is probably the fastest.
    # The idea is to keep track of the n-1, n-2, n-3 and n-4 elements
    # so that when you need the nth element you can calculate it.
    # Note: The fib4 sequence only grows by 2 each time.
    a, b, c, d = 0, 0, 2, 0
    for _ in range(n):
        d = a + b + c + d
        a, b, c, d = b, c, d, a
    return d
