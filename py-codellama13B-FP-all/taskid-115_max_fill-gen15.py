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

    # Initialize helper variables
    n = len(grid[0])
    last = 0
    times = 0
    current = [0] * n

    # Repeat until we've emptied all wells
    while sum(grid[0]) > 0:
        # Find which wells to empty
        for i in range(n):
            if grid[0][i] == 1:
                current[i] += 1
        # Add the number of wells emptied to the total
        times += sum(current)

        # Re-fill all the buckets
        for i in range(n):
            if current[i] > 0:
                current[i] = 0
        # Empty the last bucket
        current[last] = capacity
        # Move the last bucket to the beginning
        last = (last + 1) % n
    return times
