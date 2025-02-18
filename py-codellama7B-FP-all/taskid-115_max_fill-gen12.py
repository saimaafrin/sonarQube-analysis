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

    def _calc_row(row):
        """
        Calculate how many times it's possible to put water in a row
        of wells.
        """
        res = 1
        for i in range(1, len(row)):
            if row[i] != row[i-1]:
                res += 1
        return res

    res = 0
    # go through each row
    for row in grid:
        # get the max number of times the row can be filled
        row_fill = _calc_row(row)
        # calculate how much water is left to fill
        remaining = capacity - row_fill
        # if there is no water left to fill, there is no need to raise the buckets
        if remaining == 0:
            continue
        # if there is more water to fill than the number of buckets we have
        if remaining > len(row):
            # we just need to raise the number of buckets
            res += len(row)
        else:
            res += remaining
    return res
