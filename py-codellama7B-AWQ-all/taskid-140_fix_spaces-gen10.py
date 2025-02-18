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
    count = 0
    for i in range(len(text) - 1):
        if text[i] == '_' and text[i + 1] == '_':
            count += 1
    if count >= 2:
        text = text.replace('__', '-')
    return text
