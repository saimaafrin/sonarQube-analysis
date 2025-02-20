def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # print(string)
    if string.islower():
        return string.upper()
    else:
        return string.lower()
