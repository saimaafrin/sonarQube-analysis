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


    # check if a, b, c are positive numbers
    if a < 0 or b < 0 or c < 0:
        return False

    # check if the triangle is right angle triangle
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
