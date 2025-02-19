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
    # dp[i] represents the minimum path length for i values
    dp = [0] * (k + 1)
    # dp[i] is achieved from dp[i - 1] + the value on the next cell
    # so, we should store the cell value at dp[i - 1]
    # e.g. dp[k] = dp[k - 1] + next cell value
    #      dp[k - 1] = dp[k - 2] + next cell value
    #      dp[k - 2] = dp[k - 3] + next cell value
    #      ...
    #      dp[1] = next cell value
    # if dp[i - 1] contains a cell value, then we can move to the next cell
    # if dp[i - 1] is empty, then we cannot move to the next cell
    # for each cell value, it only has one direction to move
    # if the cell value is already in dp[i - 1], then it must be moved before
    # so, we should store a list of available cell values
    # e.g. if dp[i - 1] = {1, 2}
    #      then we can move to cell 1 or cell 2
    #      if we move to cell 1, then we can store dp[i] = dp[i - 1] + 1 = {1, 2, 3}
    #      if we move to cell 2, then we can store dp[i] = dp[i - 1] + 2 = {1, 2, 4}
    # for each direction, we have n * m cells
    # so, we should store a list of available directions
    dp[0] = 0
    dp[1] = grid[0][0]
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for i in range(2, k + 1):
        dp[i] = []
        for j in range(n):
            for l in range(m):
                if grid[j][l] not in dp[i - 1]:
                    continue
                for direction in directions:
                    x = j +
