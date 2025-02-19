from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    temp_string = ""
    for char in paren_string:
        if char in ["(", "{", "["]:
            stack.append(char)
            temp_string += char
        elif char in [")", "}", "]"]:
            if char == match_paren(stack.pop()):
                temp_string += char
            else:
                raise Exception(
                    "Mismatched Parentheses, can't parse string: {}".format(paren_string)
                )
        elif char == " ":
            continue
        else:
            raise Exception(
                "Invalid Parentheses, can't parse string: {}".format(paren_string)
            )

        if not stack:
            yield temp_string
            temp_string = ""
