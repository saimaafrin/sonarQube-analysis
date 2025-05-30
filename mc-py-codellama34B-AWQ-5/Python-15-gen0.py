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
    # In the following, the term "aisle" is used to refer to both horizontal and vertical aisles

    # Create a 2D matrix representing the classroom, where each position (x, y) contains a counter of the number of chatting pairs
    # that can be separated by adding an aisle at (x, y)
    chatting_matrix = [[0] * N for _ in range(M)]
    for pair in chatting_pairs:
        chatting_matrix[pair[0] - 1][pair[1] - 1] += 1
        chatting_matrix[pair[2] - 1][pair[3] - 1] += 1

    # Add the number of chatting pairs that can be separated by adding a horizontal aisle to the left of each column
    left_aisle_chatting_pairs = [0] * N
    for row in chatting_matrix:
        for i in range(N - 1):
            left_aisle_chatting_pairs[i] += row[i]

    # Add the number of chatting pairs that can be separated by adding a vertical aisle on top of each row
    top_aisle_chatting_pairs = [0] * M
    for i in range(M):
        for j in range(N):
            top_aisle_chatting_pairs[i] += chatting_matrix[i][j]

    # Optimize the placement of horizontal aisles to maximize the number of chatting pairs that can be separated
    horizontal_aisles = []
    for i in range(K):
        max_index = left_aisle_chatting_pairs.index(max(left_aisle_chatting_pairs))
        horizontal_aisles.append(max_index + 1)
        left_aisle_chatting_pairs[max_index] = 0

    # Optimize the placement of vertical aisles to maximize the number of chatting pairs that can be separated
    vertical_aisles = []
    for i in range(L):
        max_index = top_aisle_chatting_pairs.index(max(top_aisle_chatting_pairs))
        vertical_aisles.append(max_index + 1)
        top_aisle_chatting_pairs[max_index] = 0

    return (' '.join(map(str, vertical_aisles)), ' '.join(map(str, horizontal_aisles)))
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