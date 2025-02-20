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


    # Find the min path
    def findPath(g: List[List[int]], k: int, 
            row: int, col: int, values: List[int]) -> int:

        if row < 0 or col < 0 or row >= len(g) or col >= len(g[0]):
            return float('inf')
        if row == len(g) - 1 and col == len(g[0]) - 1:
            return k
        if k == 0:
            return float('inf')
        
        val = g[row][col]
        if val in values:
            return float('inf')

        values.append(val)
        m = min(findPath(g, k - 1, row, col + 1, values),
                findPath(g, k - 1, row, col - 1, values),
                findPath(g, k - 1, row - 1, col, values))
        values.pop()
        return m

    # Find the path
    pathValues = []
    minPath = findPath(grid, k, 0, 0, pathValues)

    # Reconstruct the path
    ret = []
    row, col = 0, 0
    for i in range(minPath):
        ret.append(grid[row][col])
        if col == len(grid[0]) - 1:
            row += 1
        elif row == len(grid) - 1:
            col += 1
        else:
            if grid[row][col + 1] < grid[row + 1][col]:
                col += 1
            else:
                row += 1

    return ret
