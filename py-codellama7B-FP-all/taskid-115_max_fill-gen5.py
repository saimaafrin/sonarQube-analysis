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


    # The first thing we need to do is find all the rows that have a 1.
    # This will give us a set of indices for the rows that need water.
    rows_with_water = set()
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == 1:
                rows_with_water.add(row_idx)

    # Now we need to find the longest row that has water.
    longest_row = 0
    for row_idx in rows_with_water:
        longest_row = max(longest_row, len(grid[row_idx]))

    # Start at the longest row and work our way down.
    # Whenever we reach the end of a row, we need to move down to the next row.
    current_row_idx = longest_row
    current_row_idx_offset = 0
    water_count = 0
    while current_row_idx > 0:
        # If we've reached the end of a row, move down to the next row.
        if current_row_idx_offset == len(grid[current_row_idx - 1]):
            current_row_idx -= 1
            current_row_idx_offset = 0

        # If the current index is a 1, fill up the bucket and move right.
        if grid[current_row_idx - 1][current_row_idx_offset] == 1:
            water_count += 1
            current_row_idx_offset += 1
        else:
            # If the current index is not a 1, move right.
            current_row_idx_offset += 1

    return water_count
