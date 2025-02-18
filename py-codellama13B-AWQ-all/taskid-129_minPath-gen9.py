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

    # for simplicity we add an additional row and column
    # so that we can easily check if we are at the top or left
    # and we can easily get the neighbors of each cell
    grid = [ [ 0 ] + row for row in grid ] + [ [ 0 for _ in grid[0] ] ]
    n = len(grid)
    m = len(grid[0])
    k += 1 # to simplify the implementation
    # since the minimum path is unique, we don't care about the order
    # so we can simply record the minimum values in each cell
    # and when we reach the end, we can simply go back to the beginning
    # to find the path
    visited = [ [ -1 for _ in range(m+1) ] for _ in range(n+1) ]
    for i in range(1, n+1):
        for j in range(1, m+1):
            visited[i][j] = min(visited[i-1][j], visited[i][j-1]) + grid[i-1][j-1]
    # find the minimum value
    ans = min(visited[n][j] for j in range(1, m+1))
    # find the minimum path
    i, j = n, 1
    while visited[i][j] > ans:
        i -= 1
        j += 1
    path = []
    while i > 0:
        path.append(grid[i-1][j-1])
        i -= 1
        j += 1
    path.reverse()
    return path
