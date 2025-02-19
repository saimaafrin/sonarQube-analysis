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

    # Initialize the number of times we need to lower the buckets
    # to fill all the wells
    num_fills = 0
    
    # Loop through all the rows in the grid
    for row in grid:
        # Initialize the current number of buckets needed
        # to fill the current row
        num_buckets = 0
        
        # Loop through all the wells in the current row
        for well in row:
            # If the well has water
            if well:
                # Increment the current number of buckets needed
                num_buckets += 1
                
                # If the current number of buckets needed exceeds the capacity
                # of the buckets, then we need to lower the buckets again
                if num_buckets > capacity:
                    num_fills += 1
                    num_buckets = 1
        
        # If there are still some buckets left to fill the current row
        # then we need to lower the buckets
        if num_buckets:
            num_fills += 1
    
    # Return the total number of times we need to lower the buckets
    # to fill all the wells
    return num_fills
