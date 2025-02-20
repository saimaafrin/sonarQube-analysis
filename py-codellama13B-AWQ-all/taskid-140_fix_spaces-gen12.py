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


    # replace all consecutive spaces with a single -
    text = text.replace(" ", "_")
    # replace all spaces at the beginning or end of the string with an underscore
    text = text.strip()
    # replace all spaces in the middle of the string with a -
    text = text.replace("_", "-")
    return text
