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


    # create a dictionary to store the possible paths for each cell
    paths = {0: [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]}

    # create a set to store the visited cells
    visited = set()

    # start from the cell (0, 0)
    current_cell = (0, 0)

    # start from the depth 1
    depth = 1

    # until we have visited the total cells
    while len(visited) != len(grid) ** 2:
        # if the depth is equal to k, return the path
        if depth == k:
            return [grid[i][j] for i, j in paths[k - 1]]

        # get the possible paths for the current cell
        possible_paths = paths[depth - 1]

        # for each possible path, check if the next cell is valid
        for i, j in possible_paths:
            # check if the cell is valid
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] not in visited:
                # if the cell is valid, add the cell to the visited set
                visited.add(grid[i][j])

                # if the current depth is not in the paths dictionary, add it
                if depth not in paths:
                    paths[depth] = []

                # add the current cell to the paths
                paths[depth].append((i, j))

        # increment the depth
        depth += 1

    # if the depth is equal to k, return the path
    if depth == k:
        return [grid[i][j] for i, j in paths[k - 1]]

    # if no path is found, return None
    return None
