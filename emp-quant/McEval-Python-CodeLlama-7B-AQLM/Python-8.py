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
    # Initialize the grid with the values from the input.
    grid = [[0 for _ in range(N)] for _ in range(N)]
    for x, y, value in grid_values:
        grid[y][x] = value

    # Initialize the dynamic programming table.
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Calculate the maximum sum of values collected on two paths.
    max_sum = 0
    for y in range(N):
        for x in range(N):
            # If the cell is not on the path, skip it.
            if grid[y][x] == 0:
                continue

            # Calculate the maximum sum of values collected on two paths from the cell.
            max_sum = max(max_sum, dp[y][x] + grid[y][x])

            # Calculate the maximum sum of values collected on two paths from the cell
            # to the right.
            if x < N - 1:
                max_sum = max(max_sum, dp[y][x] + dp[y][x + 1] + grid[y][x])

            # Calculate the maximum sum of values collected on two paths from the cell
            # to the bottom.
            if y < N - 1:
                max_sum = max(max_sum, dp[y][x] + dp[y + 1][x] + grid[y][x])

            # Calculate the maximum sum of values collected on two paths from the cell
            # to the bottom-right.
            if x < N - 1 and y < N - 1:
                max_sum = max(max_sum, dp[y][x] + dp[y + 1][x + 1] + grid[y][x])

            # Update the dynamic programming table.
            dp[y][x] = max_sum

    return max_sum
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