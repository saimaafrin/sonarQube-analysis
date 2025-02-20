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

    # We need to use a lookup table so we can reuse results.
    fib_cache = {
        0: 0,
        1: 0,
        2: 2,
        3: 0,
    }

    def fib4_memoized(n: int) -> int:
        if n in fib_cache:
            return fib_cache[n]
        else:
            fib_cache[n] = fib4_memoized(n - 1) + fib4_memoized(n - 2) + fib4_memoized(n - 3) + fib4_memoized(n - 4)
            return fib_cache[n]

    return fib4_memoized(n)
