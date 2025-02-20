from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:    
    >>> minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
    [1, 2, 1]

    >>> minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1)
    [1]
    """

    rows = len(grid)
    cols = len(grid[0])
    for row in grid:
        if len(row) != cols:
            raise ValueError(f"Invalid grid, {grid}")
    if rows != cols:
        raise ValueError(f"Invalid grid, {grid}")
    if k > rows * cols:
        raise ValueError(f"Invalid k {k}")

    # Initialize the grid with infinite distance from source
    grid[0][0] = 0
    for i in range(1, rows):
        grid[i][0] = float("inf")
    for i in range(1, cols):
        grid[0][i] = float("inf")

    # Calculate minimum distance of each cell
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

    # Find the shortest path and its length
    shortestPath = []
    curr_cell = (rows - 1, cols - 1)
    shortest_len = grid[curr_cell[0]][curr_cell[1]]
    while k > 0:
        shortest_len -= 1
        shortestPath.append(grid[curr_cell[0]][curr_cell[1]])
        k -= 1
        if curr_cell[0] == 0:
            curr_cell = (curr_cell[0], curr_cell[1] - 1)
        elif curr_cell[1] == 0:
            curr_cell = (curr_cell[0] - 1, curr_cell[1])
        else:
            if grid[curr_cell[0] - 1][curr_cell[1]] < grid[curr_cell[0]][curr_cell[1] - 1]:
                curr_cell = (curr_cell[0] - 1, curr_cell[1])
            else:
                curr_cell = (curr_cell[0], curr_cell[1] - 1)
    return shortestPath
