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

    dp = [0] * 5
    dp[0] = 0
    dp[1] = 0
    dp[2] = 2
    dp[3] = 0
    dp[4] = 2

    for i in range(5, n+1):
        dp[i % 5] = dp[(i-1) % 5] + dp[(i-2) % 5] + dp[(i-3) % 5] + dp[(i-4) % 5]

    return dp[n % 5]
