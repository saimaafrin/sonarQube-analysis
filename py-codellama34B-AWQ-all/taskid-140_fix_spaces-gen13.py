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

    if len(text) < 1:
        return text
    return (
        text[0].upper()
        + "".join(map(lambda c: "_" if c == " " else c, text[1:]))
        .replace("_", "")
        .replace(" ", "_")
    )
