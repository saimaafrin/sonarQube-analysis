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

    if not grid or len(grid) <= 1:
        return []

    rows, cols = len(grid), len(grid[0])
    start_cell = grid[0][0]
    end_cell = grid[-1][-1]

    dist_memo = [[float('inf')] * cols for _ in range(rows)]
    dist_memo[0][0] = 0

    # init
    cell_to_visit = [(start_cell, 0, 0)]
    visited_cells = set()

    while cell_to_visit:
        cell, r, c = cell_to_visit.pop()
        visited_cells.add(cell)

        if len(visited_cells) == k:
            break

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in visited_cells:
                cell_to_visit.append((grid[nr][nc], nr, nc))

    # construct path
    path = []
    r, c = rows-1, cols-1
    while cell != start_cell:
        path.append(cell)
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == cell:
                r, c = nr, nc
                cell = grid[r][c]
                break
    path.reverse()

    return path
