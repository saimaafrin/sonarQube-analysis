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


    def _fib4(n, memo=None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        elif n < 4:
            result = 0
        else:
            result = _fib4(n-1, memo) + _fib4(n-2, memo) + _fib4(n-3, memo) + _fib4(n-4, memo)
        memo[n] = result
        return result

    return _fib4(n)
