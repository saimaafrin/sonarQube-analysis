def plus_or_dot(pieces):
    for piece in reversed(pieces):
        if '+' in piece:
            return '.'
    return '+'