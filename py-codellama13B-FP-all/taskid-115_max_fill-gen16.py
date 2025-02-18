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

    if not grid:
        return 0

    # The first row is a special case as it can be entirely empty if all
    # wells have a value of 0.
    if not any(grid[0]):
        return 0

    # The algorithm is as follows:
    # 1. Find the maximum number of wells that can be empty by subtracting
    #    the capacity from the sum of the first row.
    # 2. Find the next row with at least 1 water in it.
    # 3. If there are more rows than wells, add the capacity to the first
    #    row and move on to the next row.
    # 4. For each row, find the number of wells that have at least 1 water in
    #    them.
    # 5. If the number of wells is less than the capacity, add the capacity to
    #    the first row and move on to the next row.
    # 6. Subtract the number of wells from the capacity.
    # 7. Move on to the next row.
    # 8. Repeat from step 3.

    wells = sum(grid[0])
    capacity_left = capacity
    row = 1
    rows_to_empty = 0
    while row < len(grid):
        rows_to_empty += 1
        wells_in_row = sum(grid[row])
        if wells_in_row > capacity_left:
            capacity_left += capacity
        elif wells_in_row < capacity_left:
            rows_to_empty += 1
            capacity_left -= wells_in_row
        row += 1
    return rows_to_empty
