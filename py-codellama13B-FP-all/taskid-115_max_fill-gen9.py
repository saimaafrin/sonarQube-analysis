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


    if capacity == 1:
        return grid.count(1)

    if capacity > 1:
        well_length = len(grid[0])
        filled_cells = grid.count(1)
        needed_buckets = filled_cells // capacity
        extra_cells = filled_cells % capacity
        if extra_cells > 0:
            needed_buckets += 1

        # Each row represents a single well, and each 1 in a row represents a single unit of water.
        # Therefore, if a row contains a 1, then you need to fill a bucket
        for row in grid:
            # Each bucket will be used once to fill a single well
            # so each row represents one bucket
            if 1 in row:
                needed_buckets += 1

        return needed_buckets

    return 0
