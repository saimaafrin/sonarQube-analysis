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

    def min_path_rec(i: int, j: int, k: int, visited: List[bool], path: List[int]) -> int:
        if k == 0:
            return 0

        visited[i * n + j] = True
        path.append(grid[i][j])

        moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        moves = [(x, y) for x, y in moves if 0 <= x < n and 0 <= y < n and not visited[x * n + y]]
        moves.sort()

        min_path_len = float('inf')
        for x, y in moves:
            min_path_len = min(min_path_len, min_path_rec(x, y, k - 1, visited, path))
        
        path.pop()
        visited[i * n + j] = False

        return min_path_len + 1

    n = len(grid)
    visited = [False] * (n ** 2)
    path = []
    min_path_len = min_path_rec(0, 0, k, visited, path)

    return path
