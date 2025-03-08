from typing import List

def tri(n: int) -> List[int]:
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    >>> tri(3)
    [1, 3, 2, 8]
    """

    if n <= 0:
        return []
    if n == 1:
        return [1]
    # Initialization
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 3
    dp[2] = 2
    # Formula
    for i in range(3, n + 1):
        if i % 2 == 0:
            dp[i] = i // 2 + 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i + 1]
    return dp[:n + 1]
