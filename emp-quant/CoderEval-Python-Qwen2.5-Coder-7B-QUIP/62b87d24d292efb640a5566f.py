def render(pieces, style):
    """
    Input pieces and a style, render the pieces to the corresponding style.
    """
    # Assuming pieces is a list of strings and style is a string
    rendered_pieces = [f"{piece} {style}" for piece in pieces]
    return rendered_pieces