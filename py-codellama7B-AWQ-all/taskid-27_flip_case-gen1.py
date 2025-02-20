def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = ''
    for character in string:
        if character.islower():
            result += character.upper()
        elif character.isupper():
            result += character.lower()
        else:
            result += character
    return result
