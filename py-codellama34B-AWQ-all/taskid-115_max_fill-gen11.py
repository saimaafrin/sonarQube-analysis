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

    # init variables
    i = 0
    j = 0
    filled = 0
    total_water = 0
    grid_length = len(grid)
    grid_width = len(grid[0])

    # loop through each well
    while i < grid_length and j < grid_width:

        # count the water in the current well
        while j < grid_width and grid[i][j] == 1:
            filled += 1
            j += 1
        total_water += min(filled, capacity)
        filled = 0
        j += 1

        # if we reach the end of a row, start a new one
        if j == grid_width:
            j = 0
            i += 1
    
    return total_water
