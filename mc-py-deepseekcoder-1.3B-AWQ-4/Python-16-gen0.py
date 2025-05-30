def count_passing_ways(n: int, m: int) -> int:
    """
    Counts the number of different ways to pass a ball among 'n' students arranged in a circle 
    such that after 'm' passes, the ball returns to the starting student.

    The function uses dynamic programming to determine the number of passing sequences. Each student
    can pass the ball either to the left neighbor or to the right neighbor.

    Args:
    n: The number of students standing in a circle.
    m: The number of times the ball is passed.

    Returns:
    An integer representing the number of distinct passing ways that result in the ball
    returning to the starting student after 'm' passes.

    Cases:
    >>> count_passing_ways(3, 3)
    2
    >>> count_passing_ways(5, 4)
    6
    """

    # Initialize the dynamic programming table.
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # If there is one person, there is only one way to pass the ball.
    for i in range(n + 1):
        dp[i][0] = 1

    # If there are more than one person, the first person can pass the ball to any student.
    # Therefore, there is only one way to pass the ball to the second person.
    for i in range(1, m + 1):
        dp[1][i] = 1

    # For each number of passes, the number of ways to pass the ball is the sum of
    # the number of ways to pass the ball to the previous student and the number of ways
    # to pass the ball to the next student.
    for i in range(2, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    # The answer is the total number of ways to pass the ball to the last student.
    return dp[m][n]
def test_count_passing_ways():
    test_cases = [
        # Test case 1: simple case
        {
            'n': 3,
            'm': 1,
            'expected': 0
        },
        # Test case 2: another simple case
        {
            'n': 4,
            'm': 2,
            'expected': 2
        },
        # Test case 3: larger number of students and passes
        {
            'n': 5,
            'm': 3,
            'expected': 0
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = count_passing_ways(test['n'], test['m'])
        assert result == test['expected'], f"Test case {i} failed: result {result} does not match expected {test['expected']}"
        print(f"Test case {i} passed with result {result}.")

# Run the test function
test_count_passing_ways()