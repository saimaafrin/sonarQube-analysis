def fix_spaces(text: str) -> str:
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    >>> fix_spaces(' Example')
    'Example'
    >>> fix_spaces(' Example 1')
    'Example_1'
    >>> fix_spaces(' Example 2')
    '_Example_2'
    >>> fix_spaces(' Example 3')
    '_Example-3'
    """


    text = text.replace(' ', '_')
    for _ in range(len(text) - 1):
        if text[-1] == ' ':
            text = text[:-1]
        elif text[-1] == '_':
            text = text[:-1]
            text = f'{text}-'
        else:
            text = f'{text}-'
    return text
