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

    
    # get the size of the grid
    n = len(grid)
    
    # create a set of the values that are not in the grid
    values = set([x for i in range(1, n*n+1) for x in [i]])
    
    # create a dictionary of the neighbors
    neighbor = {}
    
    # loop over the rows
    for i in range(n):
        for j in range(n):
            # initialize the neighbors for the current cell
            neighbor[(i, j)] = set()
            # check if the current cell is not on the edge
            if i > 0:
                # add the cell above to the neighbors
                neighbor[(i, j)].add((i-1, j))
            # check if the current cell is not on the edge
            if i < n-1:
                # add the cell below to the neighbors
                neighbor[(i, j)].add((i+1, j))
            # check if the current cell is not on the edge
            if j > 0:
                # add the cell on the left to the neighbors
                neighbor[(i, j)].add((i, j-1))
            # check if the current cell is not on the edge
            if j < n-1:
                # add the cell on the right to the neighbors
                neighbor[(i, j)].add((i, j+1))
            
            # add the current cell to the values that are not in the grid
            values.remove(grid[i][j])
    
    # create a dictionary for the best path
    best = {}
    
    # initialize the best path for each cell
    for i in range(n):
        for j in range(n):
            # initialize the best path for the current cell
            best[(i, j)] = [grid[i][j]]
    
    # loop over the values that are not in the grid
    for v in values:
        # loop over the cells
        for i in range(n):
            for j in range(n):
                # check if the current value is not in the cell
                if v != grid[i][j]:
                    # loop over the neighbors of the current cell
                    for ni, nj in neighbor[(i, j)]:
                        # check if the current value is in the neighbor
                        if v == grid[ni][nj]:
                            # get the best path for the current cell
