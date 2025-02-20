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


    # Inspired by:
    # https://www.geeksforgeeks.org/water-fill-problem/

    rows = len(grid)
    cols = len(grid[0])
    ans = 0
    curr_row = 0
    curr_col = 0

    while curr_row < rows:
        # Find the next cell that is 1 and has a capacity left.
        while curr_row < rows and grid[curr_row][curr_col] == 0:
            curr_row += 1
        if curr_row >= rows:
            break
        while curr_col < cols and grid[curr_row][curr_col] > 0 and grid[curr_row][curr_col] <= capacity:
            grid[curr_row][curr_col] -= 1
            curr_col += 1
        ans += 1
        curr_col = 0

    return ans
