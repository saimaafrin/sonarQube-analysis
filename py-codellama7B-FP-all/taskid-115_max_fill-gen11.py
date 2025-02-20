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

    max_rows = len(grid)
    max_cols = len(grid[0])
    visited = [[False for _ in range(max_cols)] for _ in range(max_rows)]
    count = 0

    for row in range(max_rows):
        for col in range(max_cols):
            if grid[row][col] == 1 and not visited[row][col]:
                count += 1
                visited[row][col] = True
                for i in range(max_rows):
                    for j in range(max_cols):
                        if grid[i][j] == 1 and visited[i][j] == False:
                            if i-row == 0 or j-col == 0:
                                visited[i][j] = True
                            elif i-row == col-j:
                                visited[i][j] = True
                                count += 1
    return count
