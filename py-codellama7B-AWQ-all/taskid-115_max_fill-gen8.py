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

    # initialize variables
    n, m = len(grid), len(grid[0])
    ans = 0
    row_sum = 0
    col_sum = 0
    row_buckets, col_buckets = [], []

    # initialize row_buckets
    for i in range(n):
        row_sum += grid[i][-1]
        row_buckets.append(row_sum)

    # initialize col_buckets
    for j in range(m):
        col_sum += grid[-1][j]
        col_buckets.append(col_sum)

    # initialize row & col
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                # if it's in the first row or first column
                if i == 0 or j == 0:
                    ans += grid[i][j]
                # if it's not in the first row or first column
                else:
                    # if it's in the middle row
                    if i == n - 1:
                        # if it's the middle column
                        if j == m - 1:
                            ans += grid[i][j]
                        # if it's not the middle column
                        else:
                            if grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
                                ans += grid[i][j]
                    # if it's in the middle column
                    elif j == m - 1:
                        # if it's the middle row
                        if i == n - 1:
                            ans += grid[i][j]
                        # if it's not the middle row
                        else:
                            if grid[i + 1][j] == 0 and grid[i - 1][j] == 0:
                                ans += grid[i][j]
                    # if it's not in the middle row
                    else:
                        # if it's in the middle row
                        if i == n - 1:
                            # if it's in the middle column
                            if j == m - 1:
                                ans += grid[i][j]
                            # if it's not in the middle column
                            else:
                                if grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
                                    ans += grid[i][j]
                        # if it's not in the middle column
                        else:
                            # if it's in the middle row
                            if j == m - 1:
