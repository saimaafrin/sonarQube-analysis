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

    rows = len(grid)
    cols = len(grid[0])
    left = [0] * cols
    right = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if i == 0:
                left[j] += grid[i][j]
            elif i == rows - 1:
                right[j] += grid[i][j]
            else:
                left[j] += grid[i][j]
                right[j] += grid[i][j]

    left_max = 0
    for i in range(cols):
        left_max = max(left_max, left[i])

    right_max = 0
    for i in range(cols):
        right_max = max(right_max, right[i])

    print(left, right, left_max, right_max)
    return max(left_max, right_max)
