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

    # initialize the number of times you need to lower the buckets
    count = 0

    # loop through the rows of the grid
    for i in range(len(grid)):
        # initialize the number of buckets needed for the current row
        buckets = 0

        # loop through the elements of the current row
        for j in range(len(grid[i])):
            # check if the current element is a well with water
            if grid[i][j] == 1:
                # increment the number of buckets needed
                buckets += 1

        # calculate the number of times you need to lower the buckets
        # for the current row
        count += buckets // capacity
    
    # return the number of times you need to lower the buckets
    return count
