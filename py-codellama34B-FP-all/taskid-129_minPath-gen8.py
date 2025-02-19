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


    # Initialize visited array to keep track of visited nodes
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize min array to keep track of the minimum distances from each cell
    # to the starting cell
    minDist = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize the queue for BFS
    queue = []
    # Mark the first cell as visited and enqueue it
    visited[0][0] = True
    queue.append([0, 0])
    # Set the min distance of first cell to 0
    minDist[0][0] = 0
    # Get the total number of cells in the grid
    cells = len(grid) * len(grid[0])

    # Do BFS until the queue is empty or k steps are taken
    while queue and k:
        # Dequeue a cell from queue and make it a part of the path
        row, col = queue.pop(0)
        # If the current cell is the last cell, return the path
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            path = []
            while row != 0 or col != 0:
                path.append(grid[row][col])
                row, col = getPrevCell(row, col, minDist)
            return path[::-1]
        # Decrease the value of k
        k -= 1
        # Get the unvisited neighbors of the dequeued cell
        neighbors = getUnvisitedNeighbors(row, col, grid, visited)
        # For each neighbor
        for neighbor in neighbors:
            # Mark it as visited and enqueue it
            rowN, colN = neighbor
            visited[rowN][colN] = True
            queue.append(neighbor)
            # Set its min distance to the min distance of the current cell plus 1
            minDist[rowN][colN] = minDist[row][col] + 1
    return []
