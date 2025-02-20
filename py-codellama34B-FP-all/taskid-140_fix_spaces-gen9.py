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


    text = text.strip()

    if len(text) <= 1:
        return text

    if text[0] == " ":
        return fix_spaces(text[1:])

    if text[-1] == " ":
        return fix_spaces(text[:-1])

    if text.count(" ") >= 3:
        return fix_spaces(text.replace("   ", "-", 1))

    return fix_spaces(text.replace("  ", "_", 1))
