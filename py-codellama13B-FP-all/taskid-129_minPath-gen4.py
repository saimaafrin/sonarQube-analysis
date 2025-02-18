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

    # Initialize our matrix
    dp = [[0] * len(grid) for _ in range(len(grid))]
    # Get the first column
    dp[0] = [j for j in grid[0]]

    # Get the first row
    for i in range(1, len(grid)):
        dp[i][0] = grid[i][0]

    # Fill in the rest
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    # Get the last column
    last_column = []
    for i in range(len(grid) - 1, -1, -1):
        last_column.append(dp[i][len(grid[0]) - 1])

    # Get the last row
    last_row = []
    for i in range(len(grid[0]) - 1, -1, -1):
        last_row.append(dp[len(grid) - 1][i])

    # Get the minimum path
    min_path = [0] * k
    i = len(grid) - 1
    j = len(grid[0]) - 1
    for p in range(k):
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
        min_path[k - p - 1] = grid[i][j]

    # Get the minimum path
    return min_path
