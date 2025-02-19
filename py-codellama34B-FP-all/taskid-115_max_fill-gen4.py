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
    water_capacity = capacity
    water_collected = 0
    bucket = []
    res = 0
    grid_height = len(grid)

    # loop through all rows in the grid
    for i in range(grid_height):
        # if bucket is empty, refill and reset collected water
        if not bucket:
            water_capacity = capacity
            water_collected = 0

        # if row is empty, skip and go to next row
        if not grid[i]:
            continue

        # if row has more water than capacity, fill the bucket with capacity
        if grid[i][0] > water_capacity:
            bucket.append(water_capacity)
            water_collected += water_capacity

        # if row has less water than capacity, fill the bucket with the row value
        else:
            bucket.append(grid[i][0])
            water_collected += grid[i][0]

        # if collected water equals capacity, empty the bucket
        if water_collected == capacity:
            res += 1
            bucket = []

    # if the remaining water in the bucket is not 0, empty the bucket
    if bucket:
        res += 1
    
    # return the number of times the bucket needs to be emptied
    return res
