from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Initialize an empty list
    output = []

    # Loop through characters in the input string
    for char in paren_string:

        # If the current character is an opening brace
        if char == '(':
            # Initialize a variable to keep track of current group's length
            length = 1
            # Initialize a variable to keep track of current group's opening braces
            opening = 1
            # Initialize a variable to keep track of current group's closing braces
            closing = 0

            # While the current group is not properly closed
            while opening != closing:
                # Get the next character in the input string
                char = paren_string[length]

                # If the current character is an opening brace
                if char == '(':
                    # Add one to the current group's opening braces
                    opening += 1

                # If the current character is a closing brace
                elif char == ')':
                    # Add one to the current group's closing braces
                    closing += 1

                # If the current character is not an opening or closing brace
                else:
                    # Do nothing
                    pass

                # Increment the current group's length
                length += 1

            # Append the current group to the output list
            output.append(paren_string[0:length])

            # Increment the current group's length
            length += 1

        # If the current character is not an opening brace
        else:
            # Do nothing
            pass

    # Return the output list
    return output
