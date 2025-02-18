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

    s1 = a + b
    s2 = b + c
    s3 = c + a
    if (s1 >= s3 and s1 >= s2) or (s2 >= s1 and s2 >= s3) or (s3 >= s2 and s3 >= s1):
        area = round(((s1 + s2 + s3) / 2) ** 0.5, 2)
        return area
    else:
        return -1
