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

    def fib4_helper(n: int, a: int, b: int, c: int, d: int) -> int:
        if n == 0:
            return d
        elif n == 1:
            return a
        elif n == 2:
            return b
        elif n == 3:
            return c
        else:
            return fib4_helper(n-1, a, b, c, d) + fib4_helper(n-2, a, b, c, d) + fib4_helper(n-3, a, b, c, d) + fib4_helper(n-4, a, b, c, d)

    return fib4_helper(n, 0, 0, 2, 0)
