def find_topmost_carpet(n, carpets, point) -> int:
    """
    Finds the topmost carpet covering a given point on the coordinate plane.

    Args:
    n (int): The total number of carpets.
    carpets (list of tuples): A list containing n tuples, each representing a carpet's information.
                              Each tuple contains four integers (a, b, g, k) where (a, b) is the
                              coordinates of the bottom-left corner of the carpet and (g, k) are
                              the lengths of the carpet along the x and y axis respectively.
    point (tuple): A tuple containing two integers (x, y), the coordinates of the point to check.

    Returns:
    int: The number of the topmost carpet covering the point (x, y), or -1 if no carpet covers it.

    Examples:
    >>> find_topmost_carpet(3, [(1, 0, 2, 3), (0, 2, 3, 3), (2, 1, 3, 3)], (2, 2))
    3
    >>> find_topmost_carpet(3, [(1, 0, 2, 3), (0, 2, 3, 3), (2, 1, 3, 3)], (4, 5))
    -1
    """

    # Create an empty list to store the max length of each carpet covering the point
    max_length = [0] * n

    # Iterate over each carpet
    for i in range(n):

        # If the point is inside the current carpet, update max_length[i]
        if (point[0] >= carpets[i][0] and point[0] <= carpets[i][0] + carpets[i][2]
                and point[1] >= carpets[i][1] and point[1] <= carpets[i][1] + carpets[i][3]):
            max_length[i] = 1

    # Find the max length and its index
    max_length_value = max(max_length)
    topmost_carpet = max_length.index(max_length_value) if max_length_value > 0 else -1

    return topmost_carpet
def check_find_topmost_carpet():
    # Test case 1: Point is on topmost carpet (carpet 3)
    assert find_topmost_carpet(3, [(1, 0, 2, 3), (0, 2, 3, 3), (2, 1, 3, 3)], (2, 2)) == 3

    # Test case 2: Point is not covered by any carpet
    assert find_topmost_carpet(3, [(1, 0, 2, 3), (0, 2, 3, 3), (2, 1, 3, 3)], (4, 5)) == -1

    # Test case 3: Point is on the edge of the carpet (carpet 1)
    assert find_topmost_carpet(2, [(1, 1, 3, 3), (4, 4, 2, 2)], (4, 1)) == 1

    # Test case 4: Point is at the corner of the carpet (carpet 2)
    assert find_topmost_carpet(2, [(1, 1, 3, 3), (4, 4, 2, 2)], (6, 4)) == 2

    # Test case 5: Multiple carpets cover the point, but the last one is on top (carpet 4)
    assert find_topmost_carpet(4, [(0, 0, 5, 5), (1, 1, 5, 5), (2, 2, 5, 5), (3, 3, 5, 5)], (4, 4)) == 4

    # Test case 6: No carpets at all, should return -1
    assert find_topmost_carpet(0, [], (0, 0)) == -1

    # Test case 8: Point is covered by the first carpet and no others (carpet 1)
    assert find_topmost_carpet(3, [(0, 0, 2, 2), (2, 2, 2, 2), (4, 4, 2, 2)], (1, 1)) == 1

    print("All test cases passed!")


# Run the test cases to ensure the function works as expected
check_find_topmost_carpet()