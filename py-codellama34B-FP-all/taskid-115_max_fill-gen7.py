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


    # Create a matrix that will contain the total units of water
    # in each well
    units = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                units[i][j] = 1
                if i > 0:
                    units[i][j] += units[i-1][j]
    
    # Create a list of the water units in each row
    units_in_each_row = [sum(row) for row in units]

    # Return the number of times you need to lower the bucket
    return sum(min(row, capacity) for row in units_in_each_row)
