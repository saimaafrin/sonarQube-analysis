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
    # Generate a map that will let us find the position of a number
    # in the grid so that we can move in the grid.
    # The map is a hash table with key as the value and value as
    # the row and col position of the value in the grid.
    value_position = {}
    for r in range(rows):
        for c in range(cols):
            value_position[grid[r][c]] = (r, c)

    def dfs(row, col, path, visited, k):
        """
        Perform a DFS to find the minimum path of length k.
        :param row: The current row
        :param col: The current col
        :param path: The path so far
        :param visited: The visited cells
        :param k: The remaining length of the path
        :return: The minimum path of length k
        """

        if k == 0:
            return path

        # Base case
        if len(path) == k:
            return path

        # If the current cell has not been visited yet
        if not visited[row][col]:
            visited[row][col] = True
            path.append(grid[row][col])

            # Try to move in 4 directions
            for new_row, new_col in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                if (
                    new_row >= 0
                    and new_row < rows
                    and new_col >= 0
                    and new_col < cols
                    and value_position[(row * cols) + col + 1]
                    == (new_row, new_col)
                ):
                    # Mark the current cell as visited
                    visited[row][col] = True

                    result = dfs(new_row, new_col, path, visited, k)

                    if result:
                        return result

                    # Backtrack
                    visited[row][col] = False
                    path.pop()

    # DFS call to find the minimum path
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    return dfs(0, 0, [], visited,
