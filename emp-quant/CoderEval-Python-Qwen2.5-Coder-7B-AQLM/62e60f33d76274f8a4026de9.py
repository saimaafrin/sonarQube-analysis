def dehydrate_point(value):
    """
    The structure class is generated based on the value length.
    """
    if len(value) == 1:
        return "Point1D"
    elif len(value) == 2:
        return "Point2D"
    elif len(value) == 3:
        return "Point3D"
    else:
        return "PointN"