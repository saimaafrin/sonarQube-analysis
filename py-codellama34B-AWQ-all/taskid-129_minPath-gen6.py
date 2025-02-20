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

    # Find the smallest value
    start = 1
    for row in grid:
        for cell in row:
            if cell < start:
                start = cell

    # Initialise min_path to start
    min_path = [start]

    # Initialise visited to false
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # Loop for k-1 steps
    for i in range(k-1):

        # Update visited to reflect the current min_path
        for cell in min_path:
            r = cell // len(grid[0])
            c = cell % len(grid[0])
            visited[r][c] = True

        # Find the next smallest value that has not been visited
        next = start + 1
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell < next and not visited[r][c]:
                    next = cell

        # Add the next value to min_path
        min_path.append(next)

    return min_path
