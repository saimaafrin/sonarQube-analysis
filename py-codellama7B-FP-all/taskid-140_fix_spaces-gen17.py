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

    result = ''
    for i in range(len(text)):
        if text[i] == ' ':
            if text[i-1] == ' ' and text[i+1] == ' ':
                result += '-'
            elif text[i-1] == ' ':
                result += '_'
            else:
                result += ' '
        else:
            result += text[i]
    return result
