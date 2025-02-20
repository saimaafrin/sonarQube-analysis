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

    # find the max number of rows to fill
    max_rows_to_fill = max([sum(row) for row in grid])

    # for each number of rows to fill, check the number of fills needed
    for rows_to_fill in range(1, max_rows_to_fill + 1):
        fills_needed = 0
        current_row = 0

        # for each row in the grid, see if it needs to be filled
        for row in grid:
            # if the row needs to be filled
            if sum(row) < rows_to_fill:
                # use up the capacity
                capacity -= rows_to_fill
                fills_needed += 1
                current_row += 1
                # reset the row to 0
                row[:] = [0] * len(row)
                # if there is no more capacity, then break out of the loop
                if capacity <= 0:
                    break
            # otherwise just increment the row
            else:
                current_row += 1

        # if no more capacity, then break out of the loop
        if capacity <= 0:
            break

    return fills_needed
