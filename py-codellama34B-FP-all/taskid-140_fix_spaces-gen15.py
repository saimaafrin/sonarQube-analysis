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

    # check if there is a space at the beginning of the string
    if text[0] == " ":
        text = "_" + text[1:]

    # check if there is a space at the end of the string
    if text[-1] == " ":
        text = text[:-1] + "_"

    # remove all space sequences from the string
    text = text.replace("  ", "_")

    return text
