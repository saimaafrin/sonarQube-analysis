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

    n = len(grid)
    m = len(grid[0])
    if n * m == 2:
        return grid[0]

    # dp[i][j] stores the minimum path of length i for the grid from top left
    # to bottom right that goes through cell (i, j)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    # initialization
    for i in range(n):
        for j in range(m):
            dp[i][j] = grid[i][j]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            # get the minimum path of length k+1 for the grid from top left to
            # bottom right that goes through cell (i, j)
            left, up = i, j+1
            if left < n:
                dp[i][j] = min(dp[i][j], dp[left][j] + grid[left][j])
            if up < m:
                dp[i][j] = min(dp[i][j], dp[i][up] + grid[i][up])
    
    return dp[0][0]
