from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """


    def _is_valid_paren_string(paren_string):
        """ Check if the input string contains a valid paren grouping.

        If the input is a valid paren grouping, we return True
        otherwise, we return False

        We don't have to worry about the spaces in the input string
        """

        # open_count keeps track of the number of open parens
        open_count = 0

        for char in paren_string:

            # if we encounter an opening paren
            if char == '(':
                # increment the count
                open_count += 1

            # if we encounter a closing paren
            elif char == ')':
                # decrement the count
                open_count -= 1

                # if the count goes negative, we have an invalid grouping
                if open_count < 0:
                    return False

        # if we get to the end of the string and the count is 0, we have a valid grouping
        if open_count == 0:
            return True
        else:
            return False

    def _separate_paren_groups(paren_string):
        """ Separate the paren groups from the input string.
        """
        # Initialize the list to return
        groups = []

        # the position where the current group starts
        group_start = 0

        # the number of open parens we've seen so far
        open_count = 0

        # keep track of the length of the string
        len_str = len(paren_string)

        for i in range(len_str):
            # if we encounter an opening paren
            if paren_string[i] == '(':
                # increment the count
                open_count += 1

            # if we encounter a closing paren
            elif paren_string[i] == ')':
                # decrement the count
                open_count -= 1

                # if the count goes to zero, we've found the end of a group
                if open_count == 0:
                    # add the group to the return list
                    groups.append(paren_string[group_start:i+1])

                    # update the starting position
                    group_start = i + 1

        # we've reached the end of the string, add the last group to the return list
        groups.append(paren_string[group_start:])

        return groups

    # first, check if the input string is valid
    if _is_valid_paren_string(paren_string):
        # separate the groups and return them
        return _separate_paren_groups(paren_string)
    else:
        # input string is invalid, return an empty list
        return []
