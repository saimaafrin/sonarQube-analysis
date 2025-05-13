from itertools import permutations

def find_number_combinations():
    """
    Generate all unique combinations of three numbers, each formed from the digits 1 to 9 without repetition,
    such that the second number is twice the first and the third is three times the first.

    Returns:
        list of tuples: A sorted list of tuples, where each tuple contains three integers representing the
                        valid number combinations in ascending order based on the first number.

    Example:
        >>> find_number_combinations()
        [(123, 246, 369), (124, 248, 372), ...]
    """
    # The possible combinations are 1-9.
    possible_combinations = [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7), (1, 2, 8), (1, 2, 9),
                             (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 3, 7), (1, 3, 8), (1, 3, 9),
                             (1, 4, 5), (1, 4, 6), (1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 5, 6),
                             (1, 5, 7), (1, 5, 8), (1, 5, 9), (1, 6, 7), (1, 6, 8), (1, 6, 9),
                             (1, 7, 8), (1, 7, 9), (1, 8, 9), (2, 3, 6), (2, 3, 7), (2, 3, 8),
                             (2, 3, 9), (2, 4, 6), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 5, 6),
                             (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 6, 7), (2, 6, 8), (2, 6, 9),
                             (2, 7, 8), (2, 7, 9), (2, 8, 9), (3, 4, 5), (3, 4, 6), (3, 4, 7),
                             (3, 4, 8), (3, 4, 9), (3, 5, 6), (3, 5, 7), (3, 5, 8), (3, 5, 9),
                             (3, 6, 7), (3, 6, 8), (3, 6, 9), (3, 7, 8), (3, 7, 9), (3, 8, 9),
                             (4, 5, 6), (4, 5, 7), (4, 5, 8), (4, 5, 9), (4, 6, 7), (4, 6, 8),
                             (4, 6, 9), (4, 7, 8), (4, 7, 9), (4, 8, 9), (5, 6, 7), (5, 6, 8),
                             (5, 6, 9), (5, 7, 8), (5, 7, 9), (5, 8, 9), (6, 7, 8), (6, 7, 9),
                             (6, 8, 9), (7, 8, 9)]

    # Filter out the combinations that do not meet the criteria.
    valid_combinations = [combo for combo in possible_combinations if combo[1] == 2 * combo[0] and combo[2] == 3 * combo[0]]

    # Sort the valid combinations.
    valid_combinations.sort()

    return valid_
def test_find_number_combinations():
    # Call the function to get the combinations
    combinations = find_number_combinations()

    # Check that we have at least one valid combination
    assert len(combinations) > 0, "There should be at least one valid combination."

    # Iterate over each combination to perform further checks
    for combo in combinations:
        # Each combination should have exactly three numbers
        assert len(combo) == 3, "Each combination should have three numbers."

        # Check if numbers are 3-digit numbers
        for num in combo:
            assert 100 <= num <= 999, f"Each number should be a 3-digit number, got {num}."

        # Check the 1:2:3 ratio
        assert combo[1] == 2 * combo[0] and combo[2] == 3 * combo[0], "The numbers should be in a 1:2:3 ratio."

    print("All test cases passed!")

# Run the test cases
test_find_number_combinations()