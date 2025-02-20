from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Step 1: Split the string by space, so that each group is a single string
    # For example: "(()()) ((())) () ((())()())" becomes ["(()())", "((()))", "()", "((())()())"]
    splitted_str = paren_string.split()
    output = []
    for group in splitted_str:
        # Step 2: Count the number of opening and closing parentheses for each group
        # For example: "(()())" has 1 opening and 1 closing parentheses, so the deepest level of nesting is 1.
        opening_parens_count = group.count("(")
        closing_parens_count = group.count(")")

        # Step 3: Calculate the deepest level of nesting.
        # For example: "((()))" has 2 opening and 2 closing parentheses, so the deepest level of nesting is 2.
        output.append(closing_parens_count - opening_parens_count)
    return output
