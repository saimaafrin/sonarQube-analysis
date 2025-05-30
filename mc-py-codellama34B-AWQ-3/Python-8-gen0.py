from typing import List, Tuple

def max_value_on_paths(N: int, grid_values: List[Tuple[int, int, int]]) -> int:
    """
    Calculate the maximum sum of values collected on two paths in an N x N grid.

    This function utilizes dynamic programming to find two paths from the top-left corner to
    the bottom-right corner of the grid which maximize the sum of the values collected. Each
    value can be collected at most once, even if both paths pass through it.

    Args:
    - N (int): The size of the grid (N x N).
    - grid_values (List[Tuple[int, int, int]]): A list of tuples where each tuple contains
      the x-coordinate, y-coordinate, and value to be placed on the grid at that position.
      The list is terminated by a tuple with all zeros.

    Returns:
    - int: The maximum sum of values collected on the two paths.

    Examples:
    >>> max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)])
    3
    >>> max_value_on_paths(8, [
    ...     (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
    ...     (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
    ...     (0, 0, 0)])
    67
    """
    # Initialize two-dimensional array with the given values.
    grid = [[0] * N for _ in range(N)]
    for x, y, value in grid_values:
        grid[x][y] = value

    # Initialize two-dimensional array of size N x N with all zeros.
    # Values in this array will hold the maximum sum of values for paths
    # that collect that value.
    dp = [[0] * N for _ in range(N)]

    # Initialize bottom row and rightmost column.
    dp[N - 1][N - 1] = grid[N - 1][N - 1]
    for i in range(N - 2, -1, -1):
        dp[N - 1][i] = max(dp[N - 1][i + 1], grid[N - 1][i])
        dp[i][N - 1] = max(dp[i + 1][N - 1], grid[i][N - 1])

    # Fill in rest of array using the recurrence relation.
    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            dp[i][j] = max(
                dp[i + 1][j],
                dp[i][j + 1],
                grid[i][j] + max(dp[i + 1][j], dp[i][j + 1]),
            )

    return dp[0][0]
def test_max_value_on_paths():
    # Test case 1: Small grid with clear path
    assert max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)]) == 3
    
    # Test case 2: Example provided in the problem statement
    assert max_value_on_paths(8, [
        (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
        (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
        (0, 0, 0)]) == 67

    print("All test cases passed!")

# Run the test cases
test_max_value_on_paths()