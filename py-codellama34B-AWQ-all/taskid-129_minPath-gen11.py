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
    # Create a 2D array with size n x n.
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    # We start from top left cell i.e. dp[0][0].
    dp[0][0] = grid[0][0]

    # Fill the first row.
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the first column.
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill the rest of the dp table.
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Create a set to store the path.
    path = set()
    i = n-1
    j = n-1
    # While we still have k steps.
    while k > 0:
        # Choose the minimum adjacent cell.
        if i-1 >= 0 and dp[i-1][j] < dp[i][j-1]:
            path.add(grid[i][j])
            i -= 1
        else:
            path.add(grid[i][j])
            j -= 1
        k -= 1

    # Return the path.
    return list(path)
