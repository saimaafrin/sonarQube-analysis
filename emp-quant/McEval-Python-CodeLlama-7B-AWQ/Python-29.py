def find_min_n_greater_than_k(k: int) -> int:
    """
    Calculate the smallest positive integer n such that the sum of the harmonic series
    up to 1/n is greater than a given positive integer k.

    The harmonic series is defined as S_n = 1 + 1/2 + 1/3 + ... + 1/n.

    Args:
    - k (int): A positive integer representing the threshold value the harmonic series sum must exceed.

    Returns:
    - int: The smallest integer n for which the harmonic series sum S_n exceeds the threshold k.

    Examples:
    >>> find_min_n_greater_than_k(1)
    2
    >>> find_min_n_greater_than_k(3)
    11
    """
    # Initialize the minimum value of n to be the largest possible value.
    min_n = float('inf')

    # Initialize the sum of the harmonic series to be 0.
    sum_harmonic_series = 0

    # Initialize the denominator of the harmonic series to be 1.
    denominator = 1

    # Iterate until the sum of the harmonic series exceeds the threshold k.
    while sum_harmonic_series < k:
        # Increment the denominator of the harmonic series by 1.
        denominator += 1

        # Add the next term to the sum of the harmonic series.
        sum_harmonic_series += 1 / denominator

        # Update the minimum value of n if the sum of the harmonic series exceeds the threshold k.
        if sum_harmonic_series > k:
            min_n = denominator

    # Return the smallest integer n for which the harmonic series sum exceeds the threshold k.
    return min_n
def test_find_min_n_greater_than_k():
    # Test case 1: k = 1, expected result is 2

    assert find_min_n_greater_than_k(1) == 2, "Test case 1 failed."

    # Test case 2: k = 3, expected result is 11
    assert find_min_n_greater_than_k(3) == 11, "Test case 2 failed."
    # Test case 3: k = 5, expected result is 83
    assert find_min_n_greater_than_k(5) == 83, "Test case 3 failed."

    print("All test cases passed.")


# Run the test function
test_find_min_n_greater_than_k()