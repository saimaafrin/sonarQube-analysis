def vertex3tuple(vertices):
    """
    Get 3 points for each vertex of the polygon.
    This will include the vertex and the 2 points on both sides of the vertex
    If the subscript is out of bounds, take the value of index as 0
    Args:
        vertices: vertices to be converted

    Returns:
        A list where the elements of vertices represented by tuple
    """
    result = []
    for i in range(len(vertices)):
        prev = vertices[i - 1] if i > 0 else vertices[i]
        next_ = vertices[(i + 1) % len(vertices)] if i < len(vertices) - 1 else vertices[i]
        result.append((prev, vertices[i], next_))
    return result