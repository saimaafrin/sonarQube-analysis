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

    # We will need to track the value of the cell, the row and the column
    # that we are currently in. We will also need to keep track of which
    # cells we have already visited. The latter is a 2D matrix of booleans
    # where True indicates that we have visited the cell and False otherwise.
    # We will also need to keep track of the current path.
    current_path = []
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # We will start at the upper left corner
    row = 0
    col = 0
    # And keep going until we reach the end of the path (k cells visited).
    while len(current_path) < k:
        # We will start by adding the current cell value to the current path
        current_path.append(grid[row][col])
        # We mark the current cell as visited
        visited[row][col] = True
        # Then we will try to go right.
        if col < cols - 1 and not visited[row][col + 1]:
            # If we can, we move right.
            col += 1
        # If we cannot go right, we try to go down.
        elif row < rows - 1 and not visited[row + 1][col]:
            # If we can, we move down.
            row += 1
        # If we cannot go down either, we try to go left.
        elif col > 0 and not visited[row][col - 1]:
            # If we can, we move left.
            col -= 1
        # If we cannot go left either, we go up.
        else:
            # If we can, we move up.
            row -= 1
    # After we have visited k cells, we return the path.
    return current_path
