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

    def bfs(graph: List[List[int]]) -> List[int]:
        """
        The graph is a grid, each cell contains a value.
        The goal is to find the minimum path of length k in the grid.
        The graph is a 2D matrix, with rows and cols.
        Each cell has at most 4 neighbors: left, right, up and down.
        The graph is undirected, meaning both left and right are equivalent.
        The graph may contain cycles.
        """
        queue = [[0, 0]]
        visited = set()
        while queue:
            row, col = queue.pop(0)
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < len(graph) and 0 <= c < len(graph[0]) and graph[r][c] != 0 and (r, c) not in visited:
                    queue.append([r, c])
                    visited.add((r, c))
            if len(queue) == 0:
                break
        return queue

    # First of all we find the cells that contains the k smallest values.
    # We need to find the cells that contains the k smallest values,
    # and these cells are the one that we will put in the min path.
    cells = sorted(grid, key=lambda cell: min(cell))[:k]
    # Now we find the minimum path of length k.
    # The minimum path is the path that starts from cell 0 and goes
    # through all cells, and the path is the shortest.
    # We are going to find the minimum path by using BFS.
    # We want to find the minimum path, so we start from the cell with
    # the minimum value. We use a queue to keep track of the cells we
    # need to visit, we add cell 0 to the queue, then we start visiting
    # the cells.
    # The queue is a list of cells, each cell contains a row and a column.
    queue = [[0, 0]]
    visited = set()
    # We will keep track of all the cells that we need to visit,
    # the visited cells are stored in a set.
    while queue:
        # We get the row and col of the cell.
        row, col = queue.pop(0)
        # We are going
