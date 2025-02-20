from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # First remove spaces
    paren_string = paren_string.replace(" ", "")
    # List of separate groups
    groups = []
    # Counter to keep track of the current group
    group_counter = 0
    # Keep track of the current group being constructed
    current_group = ""
    # Go through the string
    for char in paren_string:
        # If it's an open brace, start a new group
        if char == "(":
            group_counter += 1
            # If this is the first character in the string, don't add the character to the current group
            if current_group == "":
                continue
            # If it's not the first character, add it to the current group and move on
            else:
                current_group += char
        # If it's a close brace, stop the current group
        elif char == ")":
            # If this is the last character in the string, don't add the character to the current group
            if paren_string[paren_string.index(char) + 1] == "":
                continue
            # If it's not the last character, add it to the current group and move on
            else:
                current_group += char
            # If the brace counter is zero, we're at the end of a group. Add it to the list and reset
            if group_counter == 0:
                groups.append(current_group)
                current_group = ""
        # If the character is neither an open nor a close brace, add it to the current group
        else:
            current_group += char
    # If there are still characters left in the current group, add it to the list
    if current_group != "":
        groups.append(current_group)
    return groups
