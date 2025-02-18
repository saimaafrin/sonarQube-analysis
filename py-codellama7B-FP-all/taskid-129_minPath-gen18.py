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

    # initialize all cells with inf value
    # initialize the cells' index value in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = float("inf")
            grid[i][j] = j

    # initialize the start cell's index value
    start = 0

    # initialize the end cell's index value
    end = 0

    # initialize the size of the grid
    size = len(grid)

    # initialize the queue
    queue = []

    # initialize the current node
    current = 0

    # initialize the next node
    next = 0

    # initialize the index of the node in the queue
    index = 0

    # initialize the counter
    counter = 0

    # initialize the cell's index value
    cell = 0

    # initialize the minimum value
    min = 0

    # initialize the value of the current cell
    value = 0

    # initialize the path
    path = []

    # initialize the list of the path
    list_path = []

    # initialize the list of the list of the path
    list_list_path = []

    # initialize the index of the path
    index_path = 0

    # initialize the index of the list of the path
    index_list_path = 0

    # initialize the index of the list of the list of the path
    index_list_list_path = 0

    # initialize the final value
    final = 0

    # initialize the final path
    final_path = []

    # initialize the final list of the final path
    final_list_path = []

    # initialize the final list of the list of the final path
    final_list_list_path = []

    # initialize the start cell
    start_cell = 0

    # initialize the end cell
    end_cell = 0

    # initialize the cell's value
    cell_value = 0

    # initialize the cell's index
    cell_index = 0

    # initialize the cell's value
    cell_value = 0

    # initialize the cell's index
    cell_index = 0

    # initialize the counter
    counter = 0

    # initialize the list of the final path
    final_
