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

    from collections import defaultdict
    from heapq import heappop, heappush
    from typing import DefaultDict, List

    n = len(grid)
    if n == 2:
        return list(sorted(grid[0] + grid[1]))

    # Dict[int, List[int]]: stores the cells that need to be visited by
    # a minimum path of length k, with the values on the cells ordered.
    #
    # For example:
    #   d = { 3: [1, 2, 3], 4: [4, 5, 6], 5: [7, 8, 9] }
    #
    # means that a minimum path of length 3 goes through cells 1, 2 and 3,
    # a minimum path of length 4 goes through cells 4, 5 and 6, and a minimum
    # path of length 5 goes through cells 7, 8 and 9.
    d = defaultdict(list)
    # Dict[int, List[int]]: stores the cells that need to be visited by
    # a minimum path of length k, with the values on the cells ordered.
    #
    # For example:
    #   d = { 3: [1, 2, 3], 4: [4, 5, 6], 5: [7, 8, 9] }
    #
    # means that a minimum path of length 3 goes through cells 1, 2 and 3,
    # a minimum path of length 4 goes through cells 4, 5 and 6, and a minimum
    # path of length 5 goes through cells 7, 8 and 9.
    d_rev = defaultdict(list)

    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            d[k].append(v)
            d_rev[v].append(k)

    # List[int]: stores the values that need to be visited by a minimum path
    # of length k.
    values = list(sorted(d.keys()))

    # List[int]: stores the positions of the values in the list of values
    # that need to be visited by a minimum path of length k.
    pos = [0] * len(values)

    # DefaultDict[int, List[int]]: stores the cells that need to be
