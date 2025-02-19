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

    def get_neighbors(grid: List[List[int]]) -> List[int]:
        neighbors = []
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if row_idx - 1 >= 0:
                    neighbors.append(grid[row_idx - 1][col_idx])
                if row_idx + 1 < len(grid):
                    neighbors.append(grid[row_idx + 1][col_idx])
                if col_idx - 1 >= 0:
                    neighbors.append(grid[row_idx][col_idx - 1])
                if col_idx + 1 < len(row):
                    neighbors.append(grid[row_idx][col_idx + 1])
        return neighbors

    visited = []

    while k > 0:
        neighbors = get_neighbors(grid)
        for value in neighbors:
            if value in visited:
                visited.remove(value)

        visited.append(grid[0][0])
        k -= 1

    return visited
