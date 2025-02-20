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
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    visited = [[False] * N for _ in range(N)]
    # store the order of the values on the cells
    order = [[] for _ in range(N * N + 1)]
    # record the index of each value
    record = {}

    def dfs(x, y, step):
        if visited[x][y]:
            return
        visited[x][y] = True
        for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    order[dist[nx][ny]].append(grid[nx][ny])
                    record[grid[nx][ny]] = dist[nx][ny]
                    dfs(nx, ny, step + 1)

    dfs(0, 0, 1)

    # sort the order
    for x in order:
        x.sort()

    # return the first k values
    res = []
    i = 0
    while i < k and len(res) < N * N:
        res.append(order[i].pop(0))
        i += 1
    return res
