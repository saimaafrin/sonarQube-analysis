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


    def isValid(idx):
        row, col = idx
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

    def isPath(idx):
        # Checks if the path is valid
        row, col = idx
        return grid[row][col] == pathLen

    # Traverses the neighbors in all four directions
    def traverseNeighbors(idx):
        row, col = idx
        for r, c in [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]:
            if isValid(r, c) and (r, c) not in visited and isPath(r, c):
                yield r, c

    # Initializes the visited set
    visited = set()

    # Checks the grid size
    n = len(grid)
    assert n == len(grid[0])

    # The initial path length
    pathLen = 1

    # The minimum path is the path of length k
    minPath = []

    # The row and column of the starting cell
    startRow, startCol = 0, 0

    # Finds the starting cell
    while True:
        # If the starting cell is found, then break
        if grid[startRow][startCol] == pathLen:
            break

        # If the starting cell is not found, then iterate to the next cell
        startRow += 1

        # If the starting row is out of bounds, then iterate to the next column
        if startRow == n:
            startRow = 0
            startCol += 1

            # If the starting column is out of bounds, then the grid is invalid
            assert startCol < n

    # Adds the starting cell to the visited set
    visited.add((startRow, startCol))

    # While the path length is less than k, traverse the neighbors
    while pathLen < k:
        # Initializes the next cell
        nextCell = None

        # Finds the next cell
        for cell in traverseNeighbors((startRow, startCol)):
            # If the next cell is found, then break
            nextCell = cell
            break

        # If the next cell is not found, then the grid is invalid
        assert nextCell is not
