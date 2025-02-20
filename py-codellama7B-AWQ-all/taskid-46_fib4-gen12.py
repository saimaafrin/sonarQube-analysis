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


    # Fibonacci numbers: F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)

    # Initialize F(0), F(1), F(2), F(3)
    Fn = [0, 0, 2, 0]

    # Iterate from 4 to n
    for i in range(4, n + 1):
        # F(i) = F(i-1) + F(i-2) + F(i-3) + F(i-4)
        Fn.append(Fn[i - 1] + Fn[i - 2] + Fn[i - 3] + Fn[i - 4])

    return Fn[n]
