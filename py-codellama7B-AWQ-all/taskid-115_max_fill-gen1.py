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

    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    max_water = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                max_water += 1
                dp[i][j] = 1

            if j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1])
            if dp[i][j] > capacity:
                return max_water

    return max_water
