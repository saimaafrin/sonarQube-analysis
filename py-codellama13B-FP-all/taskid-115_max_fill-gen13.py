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

    # find the maximum number of water units that can be extracted
    # by emptying the bucket
    max_water_units = capacity
    for row in grid:
        if max_water_units > sum(row):
            max_water_units = sum(row)
    
    # empty the bucket, and for each well
    # check if it can be emptied
    # if it can be, lower the bucket
    lower_bucket = True
    for row in grid:
        if lower_bucket and sum(row) > 0:
            lower_bucket = False
        if sum(row) > max_water_units:
            lower_bucket = True

    return max_water_units
