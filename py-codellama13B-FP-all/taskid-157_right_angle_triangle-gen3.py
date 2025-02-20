def right_angle_triangle(a: int, b: int, c: int) -> bool:
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    >>> right_angle_triangle(3, 4, 5)
    True
    >>> right_angle_triangle(1, 2, 3)
    False
    """

    # 1. Check if all the three sides are not 0
    if a == 0 or b == 0 or c == 0:
        return False
    # 2. Find the square of each side
    a_sq = a * a
    b_sq = b * b
    c_sq = c * c
    # 3. Add the squares of two sides and check if they equal to the square of 
    # the third side.
    if a_sq + b_sq == c_sq or a_sq + c_sq == b_sq or b_sq + c_sq == a_sq:
        return True
    return False
