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

    """
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 4:
        return 0

    dp = [0, 0, 2, 0]
    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])

    return dp[-1]
