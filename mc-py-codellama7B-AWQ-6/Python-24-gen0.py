def count_partitions(n: int, k: int, x: int) -> int:
    """
    Count the number of ways to partition an integer n into k parts,
    where each part is at least x and order of parts does not matter.

    Parameters:
    n (int): The integer to be partitioned.
    k (int): The number of parts to divide n into.
    x (int): The minimum value for each part.

    Returns:
    int: The number of distinct partitioning ways.

    Examples:
    >>> count_partitions(7, 3, 1)
    4
    >>> count_partitions(6, 2, 1)
    3
    """

    # Validate input
    assert n > 0, 'n must be greater than zero'
    assert k > 0, 'k must be greater than zero'
    assert x > 0, 'x must be greater than zero'

    # Initialize dynamic programming table
    table = [[0] * (n + 1) for _ in range(k + 1)]

    # Populate table from right to left, top to bottom
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j < x:
                # No solutions when j is less than x
                table[i][j] = 0
            else:
                table[i][j] = table[i][j - 1] + table[i - 1][j - x]

    return table[k][n]
def test_count_partitions():
    # Test case 1: Simple case
    result = count_partitions(7, 3, 1)
    assert result == 4, f"Expected 4, got {result}"

    # Test case 2: Another simple case
    result = count_partitions(6, 2, 1)
    assert result == 3, f"Expected 3, got {result}"

    # Test case 3: Partitioning into a larger number of parts
    result = count_partitions(8, 4, 1)
    assert result == 5, f"Expected 5, got {result}"

    print("All test cases passed successfully!")


# Call the test function to run the test cases
test_count_partitions()