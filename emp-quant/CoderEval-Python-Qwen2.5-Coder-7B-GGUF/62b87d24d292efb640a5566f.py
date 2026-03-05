def render(pieces, style):
    if style == 'html':
        return '<br>'.join(pieces)
    elif style == 'markdown':
        return '\n'.join(pieces)
    elif style == 'plain':
        return ' '.join(pieces)
    else:
        raise ValueError("Unsupported style")