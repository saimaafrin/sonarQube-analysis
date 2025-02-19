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

    n = len(grid)
    assert n > 1
    assert k > 0
    assert all(len(row) == n for row in grid)
    assert all(set(cell for cell in row) == set(range(1, n * n + 1)) for row in grid)

    # 1. find the min and max
    # 2. check the min and max in the top-left corner
    # 3. check the min and max in the bottom-left corner
    # 4. check the min and max in the top-right corner
    # 5. check the min and max in the bottom-right corner
    # 6. check the min and max in the top-middle
    # 7. check the min and max in the bottom-middle
    # 8. check the min and max in the left-middle
    # 9. check the min and max in the right-middle
    # 10. return the shortest path
    # 11. ???
    # 12. profit!
