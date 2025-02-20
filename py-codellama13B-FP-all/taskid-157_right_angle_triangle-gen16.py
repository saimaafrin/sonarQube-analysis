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

    # using trigonometry
    # law of cosines: cos(B) = (a**2 + c**2 - b**2)/(2*a*c)
    # if cos(B) is 90 degree: cos(B) = 0
    return abs(cos(radians(a**2 + c**2 - b**2)/(2*a*c))) == 0
