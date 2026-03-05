def vertex3tuple(vertices):
    result = []
    n = len(vertices)
    for i in range(n):
        prev = vertices[(i - 1) % n]
        curr = vertices[i]
        next_ = vertices[(i + 1) % n]
        result.append((prev, curr, next_))
    return result