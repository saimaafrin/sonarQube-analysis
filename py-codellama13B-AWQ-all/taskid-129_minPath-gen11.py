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

    def _isValid(cell: List[int]) -> bool:
        return (cell[0] > 0 and cell[0] <= 9) and (cell[1] > 0 and cell[1] <= 9)

    def _findAdjacent(cell: List[int]) -> List[List[int]]:
        res = []
        for delta_row in [-1, 0, 1]:
            for delta_col in [-1, 0, 1]:
                if delta_row == 0 and delta_col == 0: continue
                new_cell = [cell[0] + delta_row, cell[1] + delta_col]
                if _isValid(new_cell): res.append(new_cell)
        return res

    def _sort(lst: List[int], k: int) -> List[int]:
        res = []
        for i in range(k): res.append(lst[i])
        return res

    def _minPath(grid: List[List[int]], k: int, current: List[int], path: List[int], visited: List[List[int]]) -> List[int]:
        if k == 0: return path
        visited.append(current)
        adj_cells = _findAdjacent(current)
        for cell in adj_cells:
            if cell not in visited:
                path.append(grid[cell[0] - 1][cell[1] - 1])
                visited.append(cell)
                return _minPath(grid, k - 1, cell, path, visited)
        return path

    grid_sorted = []
    for row in grid: grid_sorted.append(_sort(row, 9))

    def _search(grid_sorted: List[List[int]], current: List[int], path: List[int], visited: List[List[int]]) -> List[int]:
        if current[0] == 9 and current[1] == 9:
            return _sort(path, 9)
        visited.append(current)
        adj_cells = _findAdjacent(current)
        for cell in adj_cells:
            if cell not in visited:
                path.append(grid_sorted[cell[0] - 1][cell[1] - 1])
                visited.append(cell)
                return _search(grid_sorted, cell, path, visited
