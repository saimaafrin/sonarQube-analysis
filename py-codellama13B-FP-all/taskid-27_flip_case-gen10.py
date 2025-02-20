def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = []
    for character in string:
        if character.islower():
            result.append(character.upper())
        else:
            result.append(character.lower())
    return ''.join(result)
