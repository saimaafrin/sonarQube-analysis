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

    if n <= 3:
        return 0
    if n == 4:
        return 2
    if n >= 5:
        first = 0
        second = 0
        third = 2
        fourth = 0
        for i in range(n - 4):
            fifth = first + second + third + fourth
            first = second
            second = third
            third = fourth
            fourth = fifth
        return fifth
    return NotImplementedError("Invalid Input")
