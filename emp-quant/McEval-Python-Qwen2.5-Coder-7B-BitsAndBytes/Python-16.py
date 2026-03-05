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
    """ # Base case: If there's only one student, there's only one way to pass the ball (to themselves)
    if n == 1:
        return 1

    # Initialize a list to store the number of ways to pass the ball to each student
    ways = [0] * n

    # The first student can pass the ball to the right neighbor or to the left neighbor
    ways[0] = 2

    # Iterate over the remaining students
    for i in range(1, n):
        # The current student can pass the ball to the right neighbor or to the left neighbor
        # The number of ways to pass the ball to the right neighbor is the sum of the ways to pass
        # the ball to the left neighbor of the previous student and the ways to pass the ball to
        # the right neighbor of the previous student
        ways[i] = ways[i - 1] + ways[i - 2]

    # The number of ways to pass the ball to the last student is the sum of the ways to pass the
    # ball to the left neighbor of the last student and the ways to pass the ball to the right
    # neighbor of the last student
    return ways[n - 1] + ways[n - 2]
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