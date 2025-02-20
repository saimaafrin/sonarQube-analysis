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

    # Fill this in.
    # n is the number of the fib4 number we want to find
    # f0 is the 0th fib4 number
    # f1 is the 1st fib4 number
    # f2 is the 2nd fib4 number
    # f3 is the 3rd fib4 number
    # f4 is the 4th fib4 number
    # We can initialize these values with fib4(0) and fib4(1)
    f0, f1, f2, f3, f4 = 0, 0, 2, 0, 0
    for i in range(n):
        f0, f1, f2, f3, f4 = f1, f2, f3, f4, f0 + f1 + f2 + f3 + f4
    return f0 + f1 + f2 + f3 + f4
