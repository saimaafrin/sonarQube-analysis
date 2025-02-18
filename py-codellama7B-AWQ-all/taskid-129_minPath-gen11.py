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

    rows = len(grid)
    cols = len(grid[0])

    def get_neighbors(row, col):
        return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

    def get_neighbor_values(row, col):
        neighbors = get_neighbors(row, col)
        return [grid[r][c] for r, c in neighbors if r >= 0 and r < rows and c >= 0 and c < cols]

    def get_values_on_path(row, col, k, values):
        values.append(grid[row][col])
        neighbors = get_neighbors(row, col)
        for r, c in neighbors:
            if r >= 0 and r < rows and c >= 0 and c < cols:
                if grid[r][c] in values:
                    get_values_on_path(r, c, k - 1, values)

    def get_values_on_path_helper(row, col, k, values):
        if k == 0:
            return
        neighbors = get_neighbors(row, col)
        for r, c in neighbors:
            if r >= 0 and r < rows and c >= 0 and c < cols:
                if grid[r][c] in values:
                    get_values_on_path_helper(r, c, k - 1, values)

    def get_values_on_path_len(row, col, k, values):
        values.append(grid[row][col])
        neighbors = get_neighbors(row, col)
        for r, c in neighbors:
            if r >= 0 and r < rows and c >= 0 and c < cols:
                if grid[r][c] in values:
                    get_values_on_path_len(r, c, k - 1, values)

    def compare_path_len(path_1, path_2):
        if len(path_1) < len(path_2):
            return -1
        elif len(path_1) > len(path_2):
            return 1
        else:
            return 0

    def compare_path_values(path_1, path_2):
        if path_1
