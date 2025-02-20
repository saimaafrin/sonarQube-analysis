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


    if not grid or not capacity:
        return 0

    grid_len = len(grid)
    grid_width = len(grid[0])

    buckets = [[0 for _ in range(grid_width)] for _ in range(capacity)]
    # buckets[i][j] -> 0 | 1

    def fill_water(row_id, well_id):
        if well_id == grid_width:
            return 1

        if buckets[0][well_id] == 1:
            return 0

        if grid[row_id][well_id] == 1:
            buckets[0][well_id] = 1

            for i in range(1, capacity):
                if buckets[i][well_id] == 1:
                    continue

                buckets[i][well_id] = 1
                if fill_water(row_id, well_id + 1) == 0:
                    return 0
                buckets[i][well_id] = 0

            return 1

        return 0

    count = 0
    for row in range(grid_len):
        if fill_water(row, 0) == 1:
            count += 1

    return count
