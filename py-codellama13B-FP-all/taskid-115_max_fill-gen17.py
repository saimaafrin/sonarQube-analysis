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

    # Initialize number of buckets to 0
    total_buckets = 0

    # Iterate through grid
    for row in grid:
        # Initialize number of water units to 0
        water_units = 0

        # Iterate through row of grid
        for unit in row:
            # If water unit is 1
            if unit == 1:
                # Add 1 water unit to water units
                water_units += 1

        # If water units exceed capacity
        if water_units > capacity:
            # Add buckets needed to exceed capacity to total buckets
            total_buckets += water_units - capacity

    # Return total buckets
    return total_buckets
