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

    # Solution:
    #  1) Create an empty grid to hold the number of times a well has been drained.
    #  2) Iterate through the grid, and for each row and column, check if the water
    #     in the well is at a higher level than the bucket. If so, decrease the water
    #     in the well by the bucket level, and increment the drained well count.
    #  3) If at any point in time, the water in the well is at a level lower than the
    #     bucket level, return the number of times the well has been drained.
    #  4) The number of times the well has been drained will be the number of times
    #     the water in the well must be drained to empty the bucket.

    # Init
    grid_size = len(grid)
    drained_well = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    times_drained = 0

    # Iterate through each row and column, draining the well and updating the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # If the water is higher than the bucket, drain the well
            if grid[i][j] > capacity:
                grid[i][j] -= capacity
                drained_well[i][j] += 1
            # If the water is lower than the bucket, return the number of times
            # the well has been drained
            elif grid[i][j] < capacity:
                return times_drained

        # Update the number of times the well has been drained
        times_drained += sum(drained_well[i])

    # If all wells have been drained, return the number of times they have been drained
    return times_drained
