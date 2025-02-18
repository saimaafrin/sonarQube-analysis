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


    # Check pre-conditions
    assert len(grid) > 0
    assert len(grid[0]) > 0
    assert all(len(row) == len(grid[0]) for row in grid)
    assert capacity > 0
    assert capacity <= 10
    assert all(val in (0, 1) for row in grid for val in row)

    # Calculate the number of wells in each row.
    num_wells = len(grid[0])
    num_buckets = capacity

    # Initialize the maximum number of times to lower buckets to be the number of
    # wells.
    max_num_lowerings = num_wells

    # Iterate over the rows of the grid, starting from the bottom row.
    for i in range(num_wells - 2, -1, -1):
        # Initialize the number of lowerings to be 0.
        num_lowerings = 0

        # Iterate over the columns of the row, starting from the first.
        for j in range(num_wells):
            # If the well is empty, check if the next well is also empty.
            # If it is, then the bucket can be lowered and the well is now empty.
            if grid[i][j] == 0:
                # If the next well is empty, then the bucket can be lowered and the
                # well is now empty.
                if grid[i + 1][j] == 0:
                    num_lowerings += 1
                    grid[i][j] = 1

        # If the number of lowerings is greater than the maximum number of lowerings
        # so far, then update the maximum number of lowerings.
        if num_lowerings > max_num_lowerings:
            max_num_lowerings = num_lowerings

    # Return the maximum number of times to lower buckets.
    return max_num_lowerings
