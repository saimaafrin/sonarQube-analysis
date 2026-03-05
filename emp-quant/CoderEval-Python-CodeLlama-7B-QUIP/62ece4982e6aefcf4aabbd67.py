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
	vertices_3tuple = []
	for i in range(len(vertices)):
		if i < len(vertices) - 1:
			vertices_3tuple.append((vertices[i], vertices[i + 1], vertices[i + 2]))
		else:
			vertices_3tuple.append((vertices[i], vertices[0], vertices[1]))
	return vertices_3tuple