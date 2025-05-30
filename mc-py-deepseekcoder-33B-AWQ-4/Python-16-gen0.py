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

    # Initialize the dp array
    dp = [[0] * n for _ in range(m + 1)]

    # Base case: 1 way to pass the ball 'm' times if the starting student passes to themselves
    dp[0][0] = 1

    for i in range(1, m + 1):
        for j in range(n):
            # Calculate the left neighbor index
            left = (j - 1 + n) % n
            # Calculate the right neighbor index
            right = (j + 1) % n

            # If the ball passes to the left neighbor
            dp[i][j] += dp[i - 1][left]
            # If the ball passes to the right neighbor
            dp[i][j] += dp[i - 1][right]

    # The number of passing ways is the sum of the ways for the starting student
    return dp[m][0]
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