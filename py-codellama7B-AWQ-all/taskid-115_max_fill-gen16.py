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


    def rec(grid, row, col, capacity):
        if row == len(grid) - 1:
            return 1

        if grid[row][col] > capacity:
            return 0

        if grid[row + 1][col] - grid[row][col] > capacity:
            return 0

        max_fill = 1
        for i in range(col + 1, len(grid[0])):
            if grid[row][i] - grid[row][col] > capacity:
                break

            max_fill = max(max_fill, rec(grid, row + 1, i, capacity - grid[row][i] + grid[row][col]))

        return max_fill

    return sum(rec(grid, 0, 0, capacity) for _ in range(len(grid)))
