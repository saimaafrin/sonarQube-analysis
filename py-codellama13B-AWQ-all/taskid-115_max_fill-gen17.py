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

    # Initialize variables
    total_water = sum(map(sum, grid))
    filled_water = 0
    water_per_bucket = capacity

    # Empty the wells
    for row in grid:
        # Find the first 1 in the row
        for i in range(len(row)):
            if row[i] == 1:
                break
        
        # Count how many units of water are in the row
        for j in range(i, len(row)):
            if row[j] == 1:
                filled_water += 1
        
        # Empty the row
        for j in range(i, len(row)):
            if row[j] == 1:
                row[j] = 0
                break
    
    # Calculate the number of times the buckets must be filled
    times = filled_water // capacity
    
    return times
