def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = ''
    for letter in string:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result
