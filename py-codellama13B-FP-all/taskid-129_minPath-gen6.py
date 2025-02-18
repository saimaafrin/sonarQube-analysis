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


    # Initialize variables
    n: int = len(grid)
    m: int = len(grid[0])
    path: List[int] = []

    # Initialize the first cell
    curr_row: int = 0
    curr_col: int = 0
    path.append(grid[curr_row][curr_col])

    # Loop until the path is complete
    while len(path) != k:
        # If the current cell is on the bottom row
        if curr_row == n - 1:
            # Add the next value to the right of the current cell to the path
            curr_col += 1
            path.append(grid[curr_row][curr_col])

        # If the current cell is on the rightmost column
        elif curr_col == m - 1:
            # Add the next value below the current cell to the path
            curr_row += 1
            path.append(grid[curr_row][curr_col])

        # If the current cell is not on the bottom row or the rightmost column
        else:
            # Add the next value to the right of the current cell to the path
            curr_col += 1
            path.append(grid[curr_row][curr_col])

    # Return the path
    return path
