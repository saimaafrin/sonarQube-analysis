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
    combinations = []
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_permutations = list(permutations(digits, 9))

    for permutation in all_permutations:
        for i in range(0, len(permutation)-2):
            for j in range(i+1, len(permutation)-1):
                for k in range(j+1, len(permutation)):
                    if permutation[j] == 2*permutation[i] and permutation[k] == 3*permutation[i] and permutation[i] != 0:
                        combinations.append((int(''.join(map(str, permutation[i:j+1]))),
                                             int(''.join(map(str, permutation[j+1:k+1]))),
                                             int(''.join(map(str, permutation[k+1:])))))
    combinations.sort()

    return combinations
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