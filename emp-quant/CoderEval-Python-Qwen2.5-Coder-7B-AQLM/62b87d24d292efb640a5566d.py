def plus_or_dot(pieces):
    for piece in pieces:
        if "+" in piece:
            return "."
    return "+"