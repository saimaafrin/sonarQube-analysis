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

    # initialize variables
    rows = len(grid)
    cols = len(grid[0])
    water = 0
    filled = 0
    times = 0

    # iterate through the grid
    for i in range(rows):
        for j in range(cols):
            # if there is water in the well
            if grid[i][j] == 1:
                water += 1
            # if there is space in the bucket
            if water <= capacity:
                # fill the bucket with water
                filled += 1
                water = 0
                times += 1
            else:
                # lower the bucket
                filled -= 1
                water -= capacity
                times += 1

    return times
