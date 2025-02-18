from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    # Add a space to the end of the string because the loop below will remove the last character.
    paren_string = paren_string + " "

    # A list to hold our groups of parentheses
    group_list = []

    # The opening and closing parentheses
    open_paren = "("
    close_paren = ")"

    # The index of the last character in the string
    last_index = len(paren_string) - 1

    # The index of the current character in the string
    current_index = 0

    # This variable keeps track of whether we are in a group of parentheses
    in_parens = False

    # This variable keeps track of the number of opening and closing parens we have
    paren_count = 0

    while current_index <= last_index:
        # Get the character at the current index
        char = paren_string[current_index]

        # If we are in a group of parentheses, add it to the current group
        if in_parens:
            # If the current character is a closing paren
            if char == close_paren:
                # Decrement the paren count and if it is 0, then we are no longer in a group
                paren_count -= 1
                if paren_count == 0:
                    in_parens = False
                    current_index += 1
                    # Skip over any spaces
                    while current_index <= last_index and paren_string[current_index] == " ":
                        current_index += 1
                    continue
            # Otherwise, add the character to the group
            group_list[-1] += char
        # If we are not in a group of parentheses
        else:
            # If the current character is an opening paren
            if char == open_paren:
                # Increment the paren count and make a new group
                paren_count += 1
                in_parens = True
                group_list.append("")
            # Skip over any spaces
            while current_index <= last_index and paren_string[current_index] == " ":
                current_index += 1

        # Increment the index
        current_index += 1

    return group_list
