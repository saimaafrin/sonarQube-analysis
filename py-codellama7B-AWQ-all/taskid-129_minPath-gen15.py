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

    # Solution
    # --------
    #
    # This is a classic problem of shortest path on a weighted grid graph
    # with the following constraint:
    #
    # > Every integer in the range [1, N * N] inclusive appears exactly once
    # > on the cells of the grid.
    #
    # This problem is equivalent to finding the shortest path on a weighted
    # grid graph with the following constraint:
    #
    # > Every integer in the range [1, N * N] inclusive appears exactly once
    # > on the cells of the grid.
    #
    # The shortest path problem on a weighted grid graph is equivalent to 
    # the shortest path problem on a unweighted grid graph with the following
    # constraint:
    #
    # > There is an edge between two adjacent cells.
    #
    # The shortest path problem on a unweighted grid graph can be solved
    # using Dijkstra's algorithm in O(N) time complexity.
    #
    # References:
    #
    # - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    # - https://en.wikipedia.org/wiki/Shortest_path
    #
    # Approach:
    #
    # - Create a weighted grid graph of size N * N where every edge has a
    #   weight of 1.
    #
    # - Compute the shortest path on the grid graph using Dijkstra's algorithm.
    #
    # - Return the values on the cells that the minimum path goes through.

    # Time complexity: O(N) where N is the number of cells in the grid.
    # Space complexity: O(N) where N is the number of cells in the grid.
    # where N is the number of cells in the grid.

    # Create a weighted grid graph of size N * N where every edge has a
    # weight of 1.
    N = len(grid)
    graph = [[] for _ in range(N * N)]
    for i in range(N):
        for j in range(N):
            index = i * N + j
            if i - 1 >= 0:
                graph[index].append((index - N, 1))
            if j - 1 >= 0:
                graph[index].append((index - 1, 1))
            if i + 1 <
