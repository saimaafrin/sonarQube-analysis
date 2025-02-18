from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """


    n = len(grid)
    m = len(grid[0])
    dp = [[0] * m for _ in range(n)]

    # Initialization
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 1

    # Bottom-up DP
    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j] == 1:
                for k in range(j+1, m):
                    if grid[i][k] == 1:
                        dp[i][j] = min(dp[i][j], dp[i][k] + 1)
            dp[i][j] = min(dp[i+1][j], dp[i][j])

    # Output
    return n - 1 - max(dp[0]) if n > 1 else 0
