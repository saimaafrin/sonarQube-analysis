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

    # Transform the grid to the buckets problem
    # for each column, find the first 1, record the index
    # for each column, find the first 0 after the 1, record the index
    # get the difference between the two indices
    # then do the same thing for each row
    # then sum the results
    # then compare with the capacity
    rows = []
    cols = []
    for i, row in enumerate(grid):
        start = 0
        end = 0
        for j, cell in enumerate(row):
            if cell == 1:
                start = j
            elif cell == 0 and start != 0:
                end = j
                rows.append((start, end))
                start = 0
                end = 0

    for i, row in enumerate(grid.transpose()):
        start = 0
        end = 0
        for j, cell in enumerate(row):
            if cell == 1:
                start = j
            elif cell == 0 and start != 0:
                end = j
                cols.append((start, end))
                start = 0
                end = 0

    cols = [x for x in cols if x[1] - x[0] > 0]
    rows = [x for x in rows if x[1] - x[0] > 0]

    result = 0
    for row in rows:
        result += row[1] - row[0]

    for col in cols:
        result += col[1] - col[0]

    return result if result <= capacity else -1
