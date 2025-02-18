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

    N = len(grid)
    # Initialize dp where dp[i][j] denotes the minimum path of length i 
    # from the start cell to the cell in the jth column
    dp = [[0] * N for _ in range(k)]

    # Initialize dp[0] where dp[0][j] denotes the minimum path of length 0
    # from the start cell to the cell in the jth column
    for j in range(N):
        dp[0][j] = grid[0][j]

    for i in range(1, k):
        for j in range(N):
            # dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
            # The cell above
            up = dp[i - 1][j] if j == 0 else dp[i - 1][j - 1]
            # The cell to the right
            right = dp[i - 1][j] if j == N - 1 else dp[i - 1][j + 1]
            # The cell below
            down = dp[i - 1][j] if j == 0 else dp[i - 1][j - 1]
            dp[i][j] = min(up, right, down)

    return [dp[k - 1][i] for i in range(N)]
