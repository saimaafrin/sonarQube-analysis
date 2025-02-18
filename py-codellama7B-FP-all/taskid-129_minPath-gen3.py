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

    """
    Method: Dijkstra's Algorithm

    Time complexity: O(N * N) where N is the number of rows in the grid.
    Space complexity: O(N * N).
    """
    R, C = len(grid), len(grid[0])
    INF = 99999999999

    # Create a matrix distance to keep track of the distance from the start
    # cell to each cell.
    distance = [[INF] * C for _ in range(R)]
    # Create a matrix parent to keep track of the parent cell of each cell.
    parent = [[None] * C for _ in range(R)]

    # Initialize the distance of the start cell to 0.
    start_row, start_col = 0, 0
    distance[start_row][start_col] = 0

    for r in range(R):
        for c in range(C):
            # If the cell is not the start cell.
            if r != start_row or c != start_col:
                # Update the distance and parent if it's smaller.
                distance[r][c] = min(distance[r][c], distance[start_row][start_col] + grid[r][c])
                parent[r][c] = (start_row, start_col)

    # Loop k times to update the distance and parent.
    for _ in range(k):
        # Find the cell with the minimum distance.
        min_dist = INF
        for r in range(R):
            for c in range(C):
                if distance[r][c] < min_dist:
                    min_dist = distance[r][c]
                    min_row = r
                    min_col = c
        # Update the distance and parent for all neighboring cells.
        for r, c in [(min_row - 1, min_col), (min_row + 1, min_col), (min_row, min_col - 1), (min_row, min_col + 1)]:
            if 0 <= r < R and 0 <= c < C:
                if distance[r][c] > distance[min_row][min_col] + grid[r][c]:
                    distance[r][c] = distance[min_row][min_col] + grid[r][c]
                    parent[r][c] = (min
