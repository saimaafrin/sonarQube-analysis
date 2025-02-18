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

    # 53, 82%
    # time complexity: O(n)
    # space complexity: O(n)
    # optimized using memo
    # memo[row][col] -> number of times lowered for this row and column
    memo = [[0] * len(grid[0]) for _ in range(len(grid))]
    # init the first row, column, and the bottom row
    memo[0][0] = 1
    for i in range(len(grid[0])):
        if grid[0][i] == 1:
            memo[0][i] = 1
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[i]) - 1, -1, -1):
            if grid[i][j] == 1:
                memo[i][j] = 1
    # print(memo)
    def helper(i: int, j: int) -> int:
        # base case
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 0
        # memoization
        if memo[i][j] != 0:
            return memo[i][j]
        # recursive case
        res = 0
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            res = max(res, helper(i + 1, j) + 1)
        if i + 1 < len(grid) and j + 1 < len(grid[i + 1]) and grid[i + 1][j + 1] == 1:
            res = max(res, helper(i + 1, j + 1) + 1)
        if i > 0 and grid[i - 1][j] == 1:
            res = max(res, helper(i - 1, j) + 1)
        if i > 0 and j + 1 < len(grid[i - 1]) and grid[i - 1][j + 1] == 1:
            res = max(res, helper(i - 1, j + 1) + 1)
        memo[i][j] = res
        return res

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ans = max(ans, helper(i, j))
    return ans
