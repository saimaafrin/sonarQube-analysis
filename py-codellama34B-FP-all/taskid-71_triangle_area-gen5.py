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

    if a + b > c and a + c > b and b + c > a:
        area = 0.5 * (a * b * c)
        return round(area, 2)
    return -1
