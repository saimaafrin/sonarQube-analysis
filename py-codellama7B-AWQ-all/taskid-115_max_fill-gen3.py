from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    # transpose the matrix
    grid = list(zip(*grid))
    n = len(grid)
    grid = list(zip(*grid))

    # initialise dp, max_fill, and stack
    dp = [0] * n
    max_fill = 0
    stack = []

    # fill the first row
    for i in range(n):
        dp[i] = grid[i][0]

    # loop through the rest of the rows
    for i in range(1, n):
        for j in range(n):
            # if the current row is not 0, use that
            if grid[i][j] != 0:
                dp[j] = grid[i][j]

            # if the current row is 0 and the last row is not 0, use that
            elif dp[j] != 0 and grid[i][j] == 0:
                dp[j] = dp[j]

            # if the current row is 0 and the last row is 0, pop the stack
            elif dp[j] == 0 and grid[i][j] == 0:
                while len(stack) != 0 and stack[-1] <= j:
                    stack.pop()

        # if the dp is not 0, push it onto the stack
        if dp[n - 1] != 0:
            stack.append(n - 1)

        # if the max fill is less than the stack, update
        if len(stack) > max_fill:
            max_fill = len(stack)

    return max_fill
