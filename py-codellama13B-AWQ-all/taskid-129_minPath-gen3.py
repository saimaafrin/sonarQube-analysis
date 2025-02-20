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

    def get_neighbor(x: int, y: int) -> List[tuple]:
        """
        Return all neighbor cells
        """
        neighbors = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if 0 <= i < len(grid) and 0 <= j < len(grid):
                    neighbors.append((i, j))
        return neighbors

    def bfs(grid: List[List[int]], start: tuple, k: int) -> List[int]:
        queue = [(start, [])]
        visited = set()
        visited.add(start)
        while queue:
            (i, j), path = queue.pop(0)
            if k == 1:
                return path + [grid[i][j]]
            for neighbor in get_neighbor(i, j):
                if neighbor not in visited:
                    queue.append((neighbor, path + [grid[i][j]]))
                    visited.add(neighbor)
        return None

    res = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            res = bfs(grid, (i, j), k)
            if res:
                return res
    return None
