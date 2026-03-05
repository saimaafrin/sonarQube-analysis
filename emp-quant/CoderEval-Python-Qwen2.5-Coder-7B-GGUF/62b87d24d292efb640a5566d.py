def plus_or_dot(pieces):
    closest_tag = pieces[-1]
    if "+" in closest_tag:
        return "."
    else:
        return "+"