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

    def dfs(i: int, j: int) -> int:
        if i == n:
            return 0
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        if i == n - 1 and j == m - 1:
            return 1

        max_count = 0
        if j < m - 1:
            max_count = max(max_count, dfs(i, j + 1))
        if i < n - 1:
            max_count = max(max_count, dfs(i + 1, j))

        return max_count + 1

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += dfs(i, j)

    return count
