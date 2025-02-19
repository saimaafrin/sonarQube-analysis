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

    
    def _find_path(grid, k):
        if not grid or len(grid) < 2:
            return []

        rows = len(grid)
        cols = len(grid[0])
        cell_count = rows * cols
        if k > cell_count:
            return []

        # initialize 1-D grid for BFS
        queue = [(0, 0, 1)]
        visited = set((0, 0, 1))

        while queue:
            row, col, path = queue.pop(0)
            if k == path:
                return path
            for new_row, new_col in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] not in visited:
                    visited.add(grid[new_row][new_col])
                    queue.append((new_row, new_col, path + 1))

        return []

    def _lexicographic_compare(arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return arr1[i] < arr2[i]
        return False

    def _grid_to_list(grid):
        rows = len(grid)
        cols = len(grid[0])
        list = [0] * rows * cols
        for i in range(rows):
            for j in range(cols):
                list[i * cols + j] = grid[i][j]
        return list

    def _list_to_grid(list, rows, cols):
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = list[i * cols + j]
        return grid

    def _path_to_list(path, rows, cols):
        return [path[i * cols + j] for i in range(rows) for j in range(cols)]

    def _path_to_grid(path, rows, cols):
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
