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


    # Initialize the water level
    water = 0
    # Initialize the amount of drops
    drops = 0
    # Initialize the row index
    i = 0

    # Loop while the current row is valid
    while i < len(grid):
        # Initialize the current row
        row = grid[i]
        # Initialize the row water level
        row_water = 0
        # Loop through the row
        for j in range(len(row)):
            # Add the water from the current well to the row water level
            row_water += row[j]
        # Update the row water level
        water = max(water, row_water)
        # Update the amount of drops
        drops += 1
        # Update the row index
        i += 1

    # If the amount of water is less than or equal to the capacity
    if water <= capacity:
        # Return the amount of drops
        return drops - 1
    # Otherwise
    else:
        # Return the amount of drops
        return drops
