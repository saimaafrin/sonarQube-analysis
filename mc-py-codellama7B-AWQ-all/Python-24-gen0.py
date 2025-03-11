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
    # Check preconditions.
    assert k >= 2
    assert n >= k * x

    # Memoization table.
    memo = {}

    # Recursive function to compute the number of ways to partition n into k parts.
    def count_partitions_rec(n: int, k: int) -> int:
        if n < 0:
            return 0
        if k == 1:
            return 1
        if n == 0:
            return 1

        count = 0
        for i in range(x, n + 1):
            count += memo.get((n - i, k - 1), 0)

        memo[(n, k)] = count
        return count

    return count_partitions_rec(n, k)
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