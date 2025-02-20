from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Here is a basic outline of an algorithm that should work:
    # 1. Iterate through the input string, keeping track of the nesting level of the parentheses.
    # 2. Whenever you see a left parenthesis, increase the nesting level by 1. Whenever you see a right
    #    parenthesis, decrease the nesting level by 1.
    # 3. Whenever you see a closing parenthesis that brings the nesting level to 0, you have reached the end of
    #    a group and can return the string that has been built up so far.
    # 4. Repeat steps 2 and 3 until you reach the end of the input string.
    #
    # Here is some code to get you started:
    # parens = []
    # for char in paren_string:
    #     pass
    # return parens
    parens = []
    index = 0
    nesting_level = 0
    current_paren_group = ""
    while index < len(paren_string):
        char = paren_string[index]
        if char == '(':
            nesting_level += 1
            current_paren_group += char
        elif char == ')':
            nesting_level -= 1
            current_paren_group += char
            if nesting_level == 0:
                parens.append(current_paren_group)
                current_paren_group = ""
        else:
            # if char == ' ':
            #     continue
            current_paren_group += char
        index += 1
    return parens
