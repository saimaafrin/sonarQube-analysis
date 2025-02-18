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

    N = len(grid)

    # Initialize distance matrix
    distance = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0

    # Initialize grid matrix
    grid_copy = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            grid_copy[i][j] = grid[i][j]

    # Initialize path matrix
    path = [[0 for _ in range(N)] for _ in range(N)]

    # Breadth-First Search
    queue = deque()
    queue.append((0, 0))

    while queue:
        (x, y) = queue.popleft()
        distance[x][y] = min(distance[x][y], distance[x][y-1])
        distance[x][y] = min(distance[x][y], distance[x-1][y])

        if x < N - 1:
            distance[x][y] = min(distance[x][y], distance[x+1][y])

        if y < N - 1:
            distance[x][y] = min(distance[x][y], distance[x][y+1])

        if distance[x][y] != sys.maxsize:
            # Set path
            path[x][y] = x

            # Update queue
            if x + 1 < N and distance[x + 1][y] > distance[x][y] + grid[x + 1][y]:
                queue.append((x + 1, y))
                distance[x + 1][y] = distance[x][y] + grid[x + 1][y]
                path[x + 1][y] = x

            if y + 1 < N and distance[x][y + 1] > distance[x][y] + grid[x][y + 1]:
                queue.append((x, y + 1))
                distance[x][y + 1] = distance[x][y] + grid[x][y + 1]
                path[x][y + 1] = x

            if x - 1 >= 0 and distance[x - 1][y] > distance[x][y] + grid[x - 1][y]:
                queue.append
