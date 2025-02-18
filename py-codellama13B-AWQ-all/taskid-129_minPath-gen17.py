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

    def get_neighbors(i: int, j: int) -> List[int]:
        # returns the indices of the valid neighbors of the cell (i, j)
        if i > 0 and j > 0:
            return [(i - 1, j), (i, j - 1)]
        elif i > 0:
            return [(i - 1, j)]
        elif j > 0:
            return [(i, j - 1)]
        else:
            return []

    def get_path(current: tuple, k: int) -> List[int]:
        # returns a list containing the values on the cells that the path from
        # the current cell to a cell with value k goes through
        current_value, current_cell = current
        if current_value == k:
            return [current_value]
        else:
            for neighbor in get_neighbors(*current_cell):
                neighbor_value, neighbor_cell = neighbor
                if neighbor_value > current_value:
                    path = get_path((neighbor_value, neighbor_cell), k)
                    if path:
                        return [current_value] + path
            return []

    if k > len(grid) * len(grid[0]):
        return []

    # get the value of the top left cell
    top_left_value = grid[0][0]

    # get the path from the top left cell to the cell with the value k
    path = get_path((top_left_value, (0, 0)), k)

    # if there is no path, return an empty list
    if not path:
        return []

    # add the other values on the cells that the path goes through
    for i in range(1, len(path)):
        current_value = path[i]
        current_cell = (path[i - 1] - 1, path[i - 1] - 1)
        for neighbor in get_neighbors(current_cell[0], current_cell[1]):
            if neighbor[0] == current_cell[0] + 1 and neighbor[1] == current_cell[1] + 1:
                path[i] = grid[neighbor[0]][neighbor[1]]
                break

    return path
