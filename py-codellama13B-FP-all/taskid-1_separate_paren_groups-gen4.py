from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # This is a classic problem that requires a stack.
    # The idea is to check each bracket and add it to a stack if it is open or pop it off if it is closed.
    # If at any time the stack is not empty when you reach the end of the string, then you have an unbalanced
    # group.
    # You should be able to solve this with a stack or even just a counter. I opted for a stack.
    stack = []
    output = []
    current_output = ''

    for bracket in paren_string:
        if bracket == '(':
            stack.append(bracket)
            current_output += bracket
        elif bracket == ')':
            if len(stack) > 0:
                current_output += bracket
                stack.pop()
            else:
                current_output = ''
        elif bracket == ' ':
            if len(stack) > 0:
                current_output += bracket
        else:
            return []

        if len(stack) == 0 and current_output != '':
            output.append(current_output)
            current_output = ''
    
    return output
