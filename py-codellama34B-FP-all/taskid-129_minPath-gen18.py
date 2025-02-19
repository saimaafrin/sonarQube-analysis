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

    def path_less_than(path1: List[int], path2: List[int]) -> bool:
        """Returns True if path1 is less than path2
        """
        for i in range(min(len(path1), len(path2))):
            if path1[i] < path2[i]:
                return True
            elif path1[i] > path2[i]:
                return False
        return len(path1) < len(path2)

    def get_neighbors(r: int, c: int) -> List[int]:
        """Returns a list of the neighbor cells
        """
        neighbors = []
        if r - 1 >= 0:
            neighbors.append(grid[r - 1][c])
        if r + 1 < len(grid):
            neighbors.append(grid[r + 1][c])
        if c - 1 >= 0:
            neighbors.append(grid[r][c - 1])
        if c + 1 < len(grid[0]):
            neighbors.append(grid[r][c + 1])
        return neighbors

    def is_valid_path(path: List[int]) -> bool:
        """Checks if the path is valid
        """
        for i in range(1, len(path)):
            if path[i] not in get_neighbors(
                    get_row_column(path[i - 1])[0],
                    get_row_column(path[i - 1])[1]):
                return False
        return True

    def get_row_column(num: int) -> (int, int):
        """Returns the row and column of the number
        """
        return (num - 1) // len(grid[0]), (num - 1) % len(grid[0])

    def dfs(curr: int, path: List[int], visited: List[int], k: int) -> None:
        """Depth First Search
        """
        if len(path) == k:
            if is_valid_path(path) and path_less_than(path, best_path):
                best_path = path
        else:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] not in visited:
