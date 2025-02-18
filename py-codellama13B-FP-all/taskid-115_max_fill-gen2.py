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

    # Create a variable to keep track of the number of times we fill and empty the buckets.
    bucket_operations = 0
    # Loop through each row in the grid.
    for row in grid:
        # Find the total number of ones in the current row.
        num_ones = row.count(1)
        # If the number of ones is greater than the capacity of the bucket...
        if num_ones > capacity:
            # Add the difference between the number of ones and the capacity to the total number of operations.
            bucket_operations += num_ones - capacity
        # Else if the number of ones is less than the capacity of the bucket...
        elif num_ones < capacity:
            # Add the difference between the capacity and the number of ones to the total number of operations.
            bucket_operations += capacity - num_ones
    # Return the total number of operations.
    return bucket_operations
