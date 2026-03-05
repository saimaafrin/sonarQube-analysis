def optimize_seating(M: int, N: int, K: int, L: int, D: int, chatting_pairs: list) -> (str, str):
    """
    Optimize the placement of aisles in a classroom to minimize the amount of chatting between students.

    Args:
    M (int): The number of rows in the classroom.
    N (int): The number of columns in the classroom.
    K (int): The number of horizontal aisles to add.
    L (int): The number of vertical aisles to add.
    D (int): The number of chatting pairs in the classroom.
    chatting_pairs (list of tuples): A list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.

    Returns:
    (str, str): Two space-separated strings representing the optimal row and column indices for the aisles.

    The function works by counting the number of chatting pairs that can be separated by adding an aisle in each possible position.
    It then selects the most effective positions for aisles, aiming to separate as many chatting pairs as possible.

    Examples:
    - optimize_seating(4, 5, 1, 2, 3, [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)])
    Returns: ('2', '2 4')

    - optimize_seating(3, 3, 1, 1, 2, [(1, 2, 1, 3), (2, 1, 3, 1)])
    Returns: ('2', '2')
    """


    # Initialize counters for potential aisle positions
    row_aisle_counts = [0] * (M + 1)
    col_aisle_counts = [0] * (N + 1)

    # Count how many chatting pairs can be separated by adding an aisle at each potential position
    for pair in chatting_pairs:
        Xi, Yi, Pi, Qi = pair
        if Xi == Pi:  # Same row, vertical aisle needed
            col_aisle_counts[Yi] += 1
            col_aisle_counts[Qi + 1] -= 1
        elif Yi == Qi:  # Same column, horizontal aisle needed
            row_aisle_counts[Xi] += 1
            row_aisle_counts[Pi + 1] -= 1

    # Calculate the cumulative effect of each potential aisle position
    for i in range(1, M + 1):
        row_aisle_counts[i] += row_aisle_counts[i - 1]
    for j in range(1, N + 1):
        col_aisle_counts[j] += col_aisle_counts[j - 1]

    # Find the K most effective row and L most effective column positions
    row_aisles = sorted(range(1, M + 1), key=lambda x: row_aisle_counts[x], reverse=True)[:K]
    col_aisles = sorted(range(1, N + 1), key=lambda x: col_aisle_counts[x], reverse=True)[:L]

    # Convert the results to the required string format
    row_aisles_str = ' '.join(map(str, row_aisles))
    col_aisles_str = ' '.join(map(str, col_aisles))

    return row_aisles_str, col_aisles_str
def test_optimize_seating():
    test_cases = [
        # Test case 1 from the provided example
        {
            'M': 4, 'N': 5, 'K': 1, 'L': 2, 'D': 3,
            'chatting_pairs': [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)],
            'expected': ('2', '2 4')
        },
        # Corrected Test case 2
        {
            'M': 5, 'N': 6, 'K': 2, 'L': 3, 'D': 4,
            'chatting_pairs': [(1, 1, 1, 2), (2, 2, 3, 2), (4, 5, 4, 6), (5, 1, 5, 2)],
            'expected': ('1 2', '1 2 5')  # Corrected expected output
        },
        # Test case 3
        {
            'M': 3, 'N': 3, 'K': 1, 'L': 1, 'D': 2,
            'chatting_pairs': [(1, 2, 1, 3), (2, 1, 3, 1)],
            'expected': ('2', '2')
        },
    ]

    for i, test in enumerate(test_cases, 1):
        row_output, col_output = optimize_seating(
            test['M'], test['N'], test['K'], test['L'], test['D'], test['chatting_pairs']
        )
        assert row_output == test['expected'][0], f"Test case {i} failed: row_output {row_output} does not match expected {test['expected'][0]}"
        assert col_output == test['expected'][1], f"Test case {i} failed: col_output {col_output} does not match expected {test['expected'][1]}"
        print(f"Test case {i} passed.")

# Run the test function
test_optimize_seating()