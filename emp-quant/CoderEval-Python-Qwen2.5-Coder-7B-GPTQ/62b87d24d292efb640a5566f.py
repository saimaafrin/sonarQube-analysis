def render(pieces, style):
    if style == 'html':
        return '<br>'.join(f'<div>{piece}</div>' for piece in pieces)
    elif style == 'markdown':
        return '\n'.join(f'* {piece}' for piece in pieces)
    else:
        return '\n'.join(pieces)