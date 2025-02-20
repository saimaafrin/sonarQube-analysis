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

    """
    The idea is to use a two dimensional dp array.
    If there are two wells of size 1, then we can put them together.
    If the sum of the two wells is greater than capacity, then we cannot put them together.
    We use the value of the wells as the capacity of the bucket.
    The time complexity of this is O(n^2), where n is the number of wells.
    """
    n = len(grid)
    m = len(grid[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if grid[i - 1][j - 1] == 0:
                continue
            else:
                if i - 1 < 0 or j - 1 < 0:
                    dp[i][j] = 1
                elif dp[i - 1][j] == 0 and dp[i][j - 1] == 0:
                    dp[i][j] = 1
                elif dp[i - 1][j] == 0:
                    dp[i][j] = dp[i][j - 1]
                elif dp[i][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]
