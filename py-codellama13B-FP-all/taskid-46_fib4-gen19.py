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

    if n <= 2:
        return n
    elif n == 3:
        return 0
    else:
        fib3_1 = 0
        fib3_2 = 2
        fib3_3 = 0
        fib3_4 = 0
        for i in range(3, n):
            fib3_4 = fib3_1 + fib3_2 + fib3_3
            fib3_1 = fib3_2
            fib3_2 = fib3_3
            fib3_3 = fib3_4
        return fib3_4
