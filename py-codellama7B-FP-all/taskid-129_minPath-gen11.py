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


    def dijkstra(n, k):
        distance = [1000000000 for _ in range(n)]
        distance[0] = 0
        visited = [False for _ in range(n)]
        queue = [(0, 0)]

        while queue:
            min_node = heapq.heappop(queue)
            min_distance, node = min_node
            if visited[node]: continue
            visited[node] = True
            if distance[node] < min_distance: continue

            for neighbor in graph[node]:
                neighbor_distance = distance[node] + neighbor[1]
                if neighbor_distance < distance[neighbor[0]]:
                    distance[neighbor[0]] = neighbor_distance
                    heapq.heappush(queue, (neighbor_distance, neighbor[0]))
        return distance

    n = len(grid)
    graph = [[(i, grid[i // n][i % n]) for i in range(n * n)] for _ in range(n * n)]
    for i in range(n * n):
        for j in range(4):
            node = graph[i][j]
            if node[0] // n:
                if node[0] - n >= 0:
                    graph[i].append((node[0] - n, node[1] + grid[node[0] - n][node[0] % n]))
            if node[0] + n < n * n:
                if node[0] + n < n * n:
                    graph[i].append((node[0] + n, node[1] + grid[node[0] + n][node[0] % n]))
            if node[0] % n:
                if node[0] - 1 >= 0:
                    graph[i].append((node[0] - 1, node[1] + grid[node[0]][node[0] - 1]))
            if node[0] + 1 < n * n:
                if node[0] + 1 < n * n:
                    graph[i].append((node[0] + 1, node[1] + grid[node[0]][node[0] + 1]))
    graph = graph[k * n * n]
    print(graph)
    print(len(graph))
    print(dijkstra
