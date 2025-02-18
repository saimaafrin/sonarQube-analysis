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

    # Edge cases
    N = len(grid)
    assert N >= 2
    # The given grid is a list of lists of integers
    assert all(all(isinstance(x, int) for x in row) for row in grid)
    # k is a positive integer
    assert k > 0
    # The cells on the grid are ordered
    assert all(all(x >= 1 for x in row) for row in grid)

    # Initialize the dp table with a zeroed array of size (N * N) + 1
    dp = [0] * (N * N + 1)
    for i in range(1, N * N + 1):
        dp[i] = float('inf')

    # Initialize the queue
    queue = []
    queue.append([])

    # Loop while the queue isn't empty
    while queue:
        # Pop the last element of the queue
        node = queue.pop()

        # If the node is the one we are looking for
        if len(node) == k:
            # Return the node
            return node

        # For each neighbor of the current node
        for i in range(len(node)):
            # Get the neighbor coordinates
            x, y = divmod(i, N)
            # Get the neighbor value
            val = grid[x][y]

            # If the neighbor hasn't been visited before
            if val not in node:
                # Create a new node
                new_node = node[:]
                # Add the neighbor to the node
                new_node.append(val)
                # Push the new node to the queue
                queue.append(new_node)

    # If we didn't find a solution
    return None
