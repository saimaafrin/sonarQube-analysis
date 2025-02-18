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

    wells = []
    m = len(grid)
    n = len(grid[0])
    max_water = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                wells.append((i, j, grid[i][j]))
    
    water = 0
    turns = 0
    while water < capacity and wells:
        # sort by water
        wells.sort(key=lambda x: x[2])
        max_water = wells[0][2]
        # print(wells)
        turns += 1
        for i in range(len(wells)):
            if wells[i][2] == max_water:
                wells[i][2] = 0
                wells[i][1] -= 1
                if wells[i][1] >= 0:
                    water += 1
        # print(wells)
        # print(water, turns)
    return turns
