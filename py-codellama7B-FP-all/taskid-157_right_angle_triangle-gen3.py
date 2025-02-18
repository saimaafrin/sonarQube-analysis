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

    # check if a, b, c are all integers
    if not all(isinstance(a, int) for a in (a, b, c)):
        return False
    # check if any of the sides is 0
    if not all(a > 0 for a in (a, b, c)):
        return False
    # check if the sides are able to form a right triangle
    # this is how the formula works
    # the square of the sum of the two sides is equal to the square of the hypotenuse
    # https://en.wikipedia.org/wiki/Pythagorean_theorem
    if a*a + b*b == c*c:
        return True
    else:
        return False
