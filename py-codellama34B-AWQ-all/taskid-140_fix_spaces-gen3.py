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

    # your code here
    num_spaces = text.count(' ')
    if num_spaces == 0:
        return text
    elif num_spaces == 1:
        return text.replace(' ', '_')
    else:
        return text.replace('  ', '-', num_spaces - 1)
