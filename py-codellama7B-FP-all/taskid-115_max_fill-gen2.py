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

    row_max, col_max = len(grid), len(grid[0])
    dp = [[0] * col_max for _ in range(row_max)]
    for i in range(row_max):
        for j in range(col_max):
            if grid[i][j] == 1:
                dp[i][j] = capacity
            elif j > 0:
                dp[i][j] = min(dp[i][j-1], dp[i][j])
            else:
                dp[i][j] = 0

    for j in range(col_max):
        for i in range(row_max):
            if grid[i][j] == 1:
                dp[i][j] = min(capacity, dp[i][j])
            elif i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            else:
                dp[i][j] = 0

    res = 0
    for i in range(row_max):
        for j in range(col_max):
            if grid[i][j] == 1:
                res += dp[i][j]
    return res
