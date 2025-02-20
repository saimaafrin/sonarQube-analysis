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

    rows, columns = len(grid), len(grid[0])
    water = sum(r.count(1) for r in grid)
    if water == 0:
        return 0

    # Initialize the buckets.
    bucket_size = min(columns, capacity)
    buckets = [bucket_size] * (water // bucket_size + 1)

    # Distribute the water among the buckets.
    rows_left, cols_left = rows, columns
    bucket_index = 0
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                buckets[bucket_index] -= 1
                if buckets[bucket_index] == 0:
                    bucket_index += 1
                cols_left -= 1
                if cols_left == 0:
                    rows_left -= 1
                    cols_left = columns
                    if rows_left == 0:
                        break
        if rows_left == 0:
            break
    if rows_left == 0:
        return 0

    # Lower the buckets.
    moves = water // capacity
    if buckets[-1] > 0:
        moves += 1

    return moves
