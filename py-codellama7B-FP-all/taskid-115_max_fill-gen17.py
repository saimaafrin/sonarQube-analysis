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

    # rows, cols = len(grid), len(grid[0])
    # dp = [ [0] * cols for _ in range(rows)]
    # dp[0][0] = grid[0][0]
    # for i in range(1, rows):
    #     dp[i][0] = dp[i - 1][0] + grid[i][0]
    # for j in range(1, cols):
    #     dp[0][j] = dp[0][j - 1] + grid[0][j]
    # for i in range(1, rows):
    #     for j in range(1, cols):
    #         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # return dp[-1][-1]

    # rows, cols = len(grid), len(grid[0])
    dp = [0] * cols
    for i in range(rows):
        temp = 0
        for j in range(cols):
            temp += grid[i][j]
            dp[j] = max(dp[j], temp)
    return dp[-1]
