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

    if not grid or not grid[0] or not grid[0][0]:
        return []

    def minPathDFS(x, y, k, grid, visited):
        if not grid[x] or not grid[x][y]:
            return (0, [])

        if k == 0:
            return (grid[x][y], [grid[x][y]])

        m, n = len(grid), len(grid[0])

        visited[x][y] = True
        candidates = []
        for i in range(4):
            r, c = x + dr[i], y + dc[i]
            if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                candidates.append((r, c))

        min_val, min_path = 0, []
        for r, c in candidates:
            v, p = minPathDFS(r, c, k - 1, grid, visited)
            if v > 0 and v < min_val:
                min_val = v
                min_path = [grid[x][y]] + p

        visited[x][y] = False
        return (min_val, min_path)

    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    return minPathDFS(0, 0, k, grid, visited)[1]
