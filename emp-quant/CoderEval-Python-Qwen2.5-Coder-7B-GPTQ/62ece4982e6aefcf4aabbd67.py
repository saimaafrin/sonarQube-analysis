def vertex3tuple(vertices):
    result = []
    n = len(vertices)
    for i in range(n):
        prev = (i - 1) % n
        next_ = (i + 1) % n
        result.append((vertices[i], vertices[prev], vertices[next_]))
    return result