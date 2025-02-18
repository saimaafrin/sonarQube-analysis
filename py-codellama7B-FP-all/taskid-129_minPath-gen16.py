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
    assert n >= 2 and k >= 0
    assert all(len(row) == n for row in grid)
    assert all(1 <= cell <= n * n for row in grid for cell in row)

    # Create adjacency list
    adjacency = {}
    for i in range(n):
        for j in range(n):
            val = grid[i][j]
            if val not in adjacency:
                adjacency[val] = []
            if i > 0:
                adjacency[val].append(grid[i - 1][j])
            if i < n - 1:
                adjacency[val].append(grid[i + 1][j])
            if j > 0:
                adjacency[val].append(grid[i][j - 1])
            if j < n - 1:
                adjacency[val].append(grid[i][j + 1])

    # Create queue
    queue = [1]

    # Create visited
    visited = set()

    # Create result
    result = []

    # While queue is not empty
    while queue:
        # Pop front
        val = queue.pop(0)

        # If not visited
        if val not in visited:
            # Add to result
            result.append(val)

            # Add to visited
            visited.add(val)

            # If k reached
            if len(result) == k:
                return result

            # Add neighbors
            for neighbor in adjacency[val]:
                # If neighbor not visited
                if neighbor not in visited:
                    # Add to queue
                    queue.append(neighbor)

    # Return result
    return result
