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

    # TODO: Implement me
    # st = ''
    # i = 0
    # while i < len(text):
    #     if text[i] == ' ':
    #         if i == 0 or text[i - 1] == ' ':
    #             st += '_'
    #         else:
    #             st += '-'
    #     else:
    #         st += text[i]
    #     i += 1
    # return st
    return text.replace(" ", "_").replace("  ", "-")
