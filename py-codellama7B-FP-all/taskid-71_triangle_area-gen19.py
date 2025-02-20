def triangle_area(a: int, b: int, c: int) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    >>> triangle_area(3, 4, 5)
    6.0
    >>> triangle_area(1, 2, 10)
    -1
    """


    if a + b < c or b + c < a or a + c < b:
        return -1

    side_a_squared = a**2
    side_b_squared = b**2
    side_c_squared = c**2

    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - side_a_squared) * (s - side_b_squared) * (s - side_c_squared)) ** 0.5

    return round(area, 2)
