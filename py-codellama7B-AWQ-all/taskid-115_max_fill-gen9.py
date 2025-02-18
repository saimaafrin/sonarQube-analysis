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

    rows, cols = len(grid), len(grid[0])
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    water = sum([sum(row) for row in grid])

    def dfs(row, col, level, used, capacity):
        if row == max_row and col == max_col:
            return 1
        elif row < 0 or row >= rows or col < 0 or col >= cols:
            return 0

        cur = grid[row][col]
        used -= cur
        if used < 0:
            return 0

        # used >= 0
        next_row = row + 1
        next_col = col

        if cur == 0:
            return dfs(next_row, next_col, level + 1, used, capacity)
        else:
            # cur == 1
            if used < capacity:
                return dfs(next_row, next_col, level + 1, used, capacity)
            else:
                return dfs(next_row, next_col, level + 1, used - cur, capacity)

    def dfs_total(row, col, level, used, capacity):
        if row == max_row and col == max_col:
            return 1
        elif row < 0 or row >= rows or col < 0 or col >= cols:
            return 0

        cur = grid[row][col]
        used -= cur
        if used < 0:
            return 0

        # used >= 0
        next_row = row + 1
        next_col = col

        if cur == 0:
            return dfs_total(next_row, next_col, level + 1, used, capacity)
        else:
            # cur == 1
            if used < capacity:
                return dfs_total(next_row, next_col, level + 1, used, capacity)
            else:
                return dfs_total(next_row, next_col, level + 1, used - cur, capacity)

    dfs_total(0, 0, 0, water, capacity)
    return dfs(0, 0, 0, water, capacity)
