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

    rows, cols = len(grid), len(grid[0])
    max_row, max_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_row = i
                max_col = j
                break
    if rows == 1 and cols == 1:
        return 0
    if max_row == 0 and max_col == 0:
        return 0
    #print(max_row, max_col)

    # find the farthest left and right wells
    left_well = right_well = -1
    for i in range(max_row, -1, -1):
        if grid[i][max_col] == 1:
            left_well = i
            break
    for i in range(max_row, rows):
        if grid[i][max_col] == 1:
            right_well = i
            break
    #print(left_well, right_well)

    # find the farthest top and bottom wells
    top_well = bottom_well = -1
    for j in range(max_col, -1, -1):
        if grid[max_row][j] == 1:
            top_well = j
            break
    for j in range(max_col, cols):
        if grid[max_row][j] == 1:
            bottom_well = j
            break
    #print(top_well, bottom_well)

    # count the number of wells that are not at the edge
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                continue
            if grid[i][j] == 1:
                cnt += 1
    #print(cnt)

    #print(max_row, max_col, left_well, right_well, top_well, bottom_well)
    # return the number of moves
    return max(cnt, rows - max_row + 1, cols - max_col + 1,
                rows - left_well + 1, rows - right_well + 1,
                cols - top_well + 1, cols - bottom_well + 1)
