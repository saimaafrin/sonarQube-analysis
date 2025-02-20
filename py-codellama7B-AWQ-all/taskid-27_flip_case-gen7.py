def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    new_string = ""
    for character in string:
        if character.islower():
            new_string += character.upper()
        else:
            new_string += character.lower()
    return new_string
