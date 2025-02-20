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

    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < n and 0 <= col < n

    def neighbors(row: int, col: int) -> List[List[int]]:
        return [[row - 1, col], [row, col - 1], [row, col + 1], [row + 1, col]]

    n = len(grid)

    queue = []
    visited = set()
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                queue.append([(row, col)])
                visited.add((row, col))
                break

    while queue:
        path = queue.pop(0)
        if len(path) == k:
            return [grid[row][col] for row, col in path]

        row, col = path[-1]
        for new_row, new_col in neighbors(row, col):
            if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                new_path = path.copy()
                new_path.append((new_row, new_col))
                queue.append(new_path)

    return []
