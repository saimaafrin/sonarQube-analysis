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

    max_fills = 0

    # find the width and height of the grid
    grid_width = len(grid[0])
    grid_height = len(grid)

    for i in range(grid_height):
        for j in range(grid_width):
            # if we found a 1 in a well
            if grid[i][j] == 1:
                # if there is a 1 in the well to the right of the current one
                if j < grid_width - 1 and grid[i][j + 1] == 1:
                    max_fills += 1

                    # if there is a 1 in the well to the right of the current one,
                    # and in the well above the current one, and below the current one
                    # and above the well to the right of the current one
                    if i > 0 and i < grid_height - 1:
                        if grid[i - 1][j + 1] == 1 and grid[i + 1][j + 1] == 1:
                            max_fills += 1

                    # if there is a 1 in the well above the current one
                    # and above the well to the right of the current one
                    if i > 0:
                        if grid[i - 1][j] == 1 and grid[i - 1][j + 1] == 1:
                            max_fills += 1

                    # if there is a 1 in the well below the current one
                    # and below the well to the right of the current one
                    if i < grid_height - 1:
                        if grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1:
                            max_fills += 1

                    # if there is a 1 in the well below the current one
                    # and below the well to the right of the current one
                    # and below the well above the current one
                    if i < grid_height - 1 and i > 0:
                        if grid[i - 1][j] == 1 and grid[i + 1][j] == 1:
                            max_fills += 1

    return max_fills
