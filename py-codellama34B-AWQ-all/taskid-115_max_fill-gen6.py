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

    rows, cols = len(grid), len(grid[0])
    # Initialize the water level for each row
    water_level = [0] * rows

    # Traverse each row
    for row in range(rows):
        # Keep track of the amount of water we can fill in this row
        row_capacity = capacity

        # Traverse each column in the row
        for col in range(cols):
            # If the current water level is less than the current cell's water level,
            # then we need to lower the bucket
            if water_level[row] < grid[row][col]:
                # Calculate the difference between the current cell's water level
                # and the current water level in this row
                diff = grid[row][col] - water_level[row]

                # If the difference is less than the row capacity, then we can fill
                # the entire difference with the bucket
                if diff <= row_capacity:
                    water_level[row] += diff
                    row_capacity -= diff
                # If the difference is greater than the row capacity, then we can only
                # fill the row capacity
                else:
                    water_level[row] += row_capacity
                    row_capacity = 0

    return capacity * rows - sum(water_level)
