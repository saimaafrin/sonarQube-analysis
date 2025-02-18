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


    m = len(grid)
    if m == 1:
        return grid[0][:k]
    
    n = len(grid[0])
    if n == 1:
        return [ grid[i][0] for i in range(k) ]

    assert m == n
    assert k <= m * n
    
    # build a graph, each node represents a cell, each edge represents a
    # neighbor
    G = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            if i - 1 >= 0:
                G[i * n + j].append((i - 1, j))
            if i + 1 < m:
                G[i * n + j].append((i + 1, j))
            if j - 1 >= 0:
                G[i * n + j].append((i, j - 1))
            if j + 1 < n:
                G[i * n + j].append((i, j + 1))

    # build a shortest path graph, each node represents a cell, each edge
    # represents the shortest distance from a cell to another cell
    dist = [ float('inf') ] * (m * n)
    dist[0] = 0
    Q = [ 0 ]
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                Q.append(v)
    dist = dist[:m * n]

    # find the shortest path
    min_dist = float('inf')
    min_path = []
    for i in range(m):
        for j in range(n):
            if dist[i * n + j] < min_dist:
                min_dist = dist[i * n + j]
                min_path = [grid[i][j] for i in range(m)]
    assert min_dist == k
    return min_path
