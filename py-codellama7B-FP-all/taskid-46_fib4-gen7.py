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

    def fib4_recursive(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        return fib4_recursive(n - 1) + fib4_recursive(n - 2) + fib4_recursive(n - 3) + fib4_recursive(n - 4)

    def fib4_iterative(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        fib4_list = [0] * (n + 1)
        fib4_list[0] = 0
        fib4_list[1] = 0
        fib4_list[2] = 2
        for i in range(3, n + 1):
            fib4_list[i] = fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4]
        return fib4_list[n]

    print(fib4_iterative(n))
