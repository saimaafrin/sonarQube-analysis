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

    # A matrix is not a grid
    assert len(grid) == len(grid[0]), "A matrix is not a grid"
    # Get the size of the grid
    n = len(grid)
    # Define a matrix to store the minimum distances
    d = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Define a matrix to store the previous nodes
    p = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Define a matrix to store the nodes to visit
    q = [[float('inf') for _ in range(n)] for _ in range(n)]
    # Fill the distance matrix
    for i in range(n):
        for j in range(n):
            d[i][j] = grid[i][j]
            p[i][j] = -1
            q[i][j] = -1
    # Set the starting point
    s = 0
    # Set the ending point
    e = n - 1
    # Set the starting index
    si = 0
    # Set the ending index
    ei = 0
    # Set the initial distance
    d[s][e] = 0
    # Set the initial previous distance
    p[s][e] = -1
    # Set the initial distance to visit
    q[s][e] = 0
    # Set the initial number of steps
    nbSteps = 0
    # Set the number of steps to do
    nbSteps = (n * n) - 1
    while nbSteps > 0:
        # Set the new number of steps
        nbSteps = 0
        # Loop on the rows
        for i in range(n):
            # Loop on the columns
            for j in range(n):
                # If the current node is not the starting node
                if i != s or j != e:
                    # If the current node is not the ending node
                    if i != e or j != s:
                        # If the current node is not visited
                        if q[i][j] < 0:
                            # If the current node is not the starting node
                            if i != s:
                                # If the previous node is not the starting node
                                if p[i][j] != -1:
                                    # Update the previous node
                                    p[i][j] =
