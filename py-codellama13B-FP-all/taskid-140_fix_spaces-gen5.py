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

    # Check if input is a string
    assert isinstance(text, str), "Input must be of type string"

    # Replace multiple spaces with single space
    text = " ".join(text.split())

    # Replace spaces with underscores
    text = text.replace(" ", "_")

    # Replace consecutive spaces with -
    text = text.replace("__", "-")

    # Remove leading and trailing underscores
    text = text.strip("_")

    return text
