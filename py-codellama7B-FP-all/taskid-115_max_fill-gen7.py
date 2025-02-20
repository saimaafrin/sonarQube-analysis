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

    m, n = len(grid), len(grid[0])
    rows_to_drop, cols_to_drop = 0, 0
    while rows_to_drop < m and cols_to_drop < n:
        rows_to_drop += 1
        cols_to_drop += 1
        cur_row_max = -1
        cur_col_max = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] > cur_row_max:
                    cur_row_max = grid[i][j]
                if grid[j][i] > cur_col_max:
                    cur_col_max = grid[j][i]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == cur_row_max:
                    grid[i][j] = 0
                if grid[j][i] == cur_col_max:
                    grid[j][i] = 0

    return m + n - 2*rows_to_drop - 2*cols_to_drop
