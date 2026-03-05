def minimum_students_to_leave(heights):
    """
    Calculate the minimum number of students that need to leave to form a choir formation.
    A choir formation is defined such that for some position 'i', the heights of students
    increase from the start to 'i' and decrease from 'i' to the end of the formation.

    Args:
    heights (List[int]): A list of student heights.

    Returns:
    int: The minimum number of students that need to leave.
    """
    n = len(heights)
    if n < 2:
        return 0

    # Initialize the left and right arrays to store the longest increasing subsequence
    # ending at each index from the left and right respectively.
    left = [1] * n
    right = [1] * n

    # Calculate the longest increasing subsequence from the left
    for i in range(1, n):
        for j in range(i):
            if heights[i] > heights[j]:
                left[i] = max(left[i], left[j] + 1)

    # Calculate the longest increasing subsequence from the right
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if heights[i] > heights[j]:
                right[i] = max(right[i], right[j] + 1)

    # Find the maximum length of the increasing subsequence that can be formed
    max_length = 0
    for i in range(n):
        max_length = max(max_length, left[i] + right[i] - 1)

    # The minimum number of students to leave is the total number of students minus
    # the maximum length of the increasing subsequence that can be formed.
    return n - max_length
def test_minimum_students_to_leave():
    # Test case 1: Provided example
    assert minimum_students_to_leave([186, 186, 150, 200, 160, 130, 197, 220]) == 4, "Test case 1 failed"

    # Test case 2: All students have the same height
    assert minimum_students_to_leave([150, 150, 150, 150, 150]) == 4, "Test case 2 failed"

    # Test case 3: Students are already in a choir formation
    assert minimum_students_to_leave([130, 150, 170, 190, 170, 150, 130]) == 0, "Test case 3 failed"

    # Test case 4: Students are in strictly increasing order
    assert minimum_students_to_leave([130, 135, 140, 145, 150, 155]) == 0, "Test case 4 failed"

    # Test case 5: Students are in strictly decreasing order
    assert minimum_students_to_leave([155, 150, 145, 140, 135, 130]) == 0, "Test case 5 failed"

    # Test case 6: Optimal choir formation is not including the first or last student
    assert minimum_students_to_leave([200, 180, 190, 170, 210, 160, 220]) == 3, "Test case 6 failed"

    print("All test cases passed!")

# Run the test function
test_minimum_students_to_leave()