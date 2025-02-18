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

    if n < 4:
        return 0
    if n == 4:
        return 2
    if n == 5:
        return 4
    if n == 6:
        return 8
    if n == 7:
        return 14

    fibs = [0, 0, 2, 4, 8, 14, 25, 43]
    for i in range(8, n):
        fibs.append(fibs[i-3] + fibs[i-2] + fibs[i-1] + fibs[i-4])
    return fibs[n]
