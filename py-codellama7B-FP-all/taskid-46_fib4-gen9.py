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

    # initialize the 4 variables
    a, b, c, d = 0, 0, 0, 0
    for i in range(n+1):
        if i == 0:
            a = 0
        elif i == 1:
            b = 0
        elif i == 2:
            c = 2
        elif i == 3:
            d = 0
        else:
            a = b
            b = c
            c = d
            d = a + b + c + d
    return d
