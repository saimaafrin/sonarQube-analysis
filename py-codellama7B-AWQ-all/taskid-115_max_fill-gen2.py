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

    # the idea is to go through each well and check if its water can be filled,
    # if it can, then the number of times that the bucket should be moved is the number of times that the bucket is moved to that well
    # if it cannot, the number of times that the bucket should be moved is the number of times that the bucket is moved to the next well
    # this can be done with a simple loop through each row

    bucket_moves = 0
    for row in range(len(grid)):
        current_move = 0
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                current_move += 1
            else:
                bucket_moves += current_move
                current_move = 0
        bucket_moves += current_move
    return bucket_moves // capacity
