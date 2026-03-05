def vertex3tuple(vertices):
    n = len(vertices)
    result = []
    for i in range(n):
        prev = vertices[(i - 1) % n]
        current = vertices[i]
        next_ = vertices[(i + 1) % n]
        result.append((prev, current, next_))
    return result