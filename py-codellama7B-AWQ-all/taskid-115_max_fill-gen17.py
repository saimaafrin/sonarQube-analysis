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

    assert len(grid[0]) == len(grid[1])
    num_rows = len(grid)
    num_cols = len(grid[0])
    bucket_count = num_rows
    water_count = 0

    # keep track of how many water wells were filled by each bucket
    bucket_fills = [0] * bucket_count

    for row in range(num_rows):
        # keep track of how many water wells were filled in the current row
        row_fill = 0
        for col in range(num_cols):
            # if the water level of this well is 1
            if grid[row][col] == 1:
                # if there are no water wells filled in this row
                if row_fill == 0:
                    # start filling this well with the current bucket
                    bucket_fills[row] += 1
                    row_fill += 1
                    water_count += 1
                    if water_count == capacity:
                        return capacity
                # if there is already at least one water well filled in this row
                else:
                    # fill this well with the current bucket
                    bucket_fills[row] += 1
                    row_fill += 1
                    water_count += 1
                    if water_count == capacity:
                        return capacity
            # if the water level of this well is 0
            else:
                # if there are no water wells filled in this row
                if row_fill == 0:
                    pass
                # if there is already at least one water well filled in this row
                else:
                    # finish filling this well with the current bucket
                    bucket_fills[row] += 1
                    row_fill += 1
                    water_count += 1
                    if water_count == capacity:
                        return capacity

    # return the total number of times a bucket was used
    return sum(bucket_fills)
