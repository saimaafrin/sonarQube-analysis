def render(pieces, style):
    """
    Input pieces and a style, render the pieces to the corresponding style.
    """
    if style == 'html':
        return '<br>'.join(f'<div>{piece}</div>' for piece in pieces)
    elif style == 'markdown':
        return '\n'.join(f'**{piece}**' for piece in pieces)
    else:
        return ' '.join(pieces)