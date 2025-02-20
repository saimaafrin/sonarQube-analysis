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

    def min_path(grid: List[List[int]], k: int) -> List[int]:
        """Returns the minimum path of length k in the grid. """
        n = len(grid)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = grid[i][j]
        for l in range(1, k):
            for i in range(n):
                for j in range(n):
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 2):
                            if 0 <= a < n and 0 <= b < n and (a != i or b != j):
                                dp[i][j][l] = min(dp[i][j][l], dp[a][b][l - 1])
        return [dp[i][j][k - 1] for i in range(n) for j in range(n)]

    # 292 ms, faster than 73.11% of Python3 online submissions for Minimum Path Cost in a Grid with Obstacles Elimination.
    # 16 MB, less than 76.91% of Python3 online submissions for Minimum Path Cost in a Grid with Obstacles Elimination.
    def min_path_2(grid: List[List[int]], k: int) -> List[int]:
        """Returns the minimum path of length k in the grid. """
        n = len(grid)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = grid[i][j]
        for l in range(1, k):
            for i in range(n):
                for j in range(n):
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 2):
                            if 0 <= a < n and 0 <= b < n and (a != i or b != j):
                                dp[i][j][l] = min(dp[i][j][l],
