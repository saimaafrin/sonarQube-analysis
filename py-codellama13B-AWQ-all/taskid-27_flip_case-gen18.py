def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    if string.islower():
        return string.upper()
    elif string.isupper():
        return string.lower()
    else:
        return string
