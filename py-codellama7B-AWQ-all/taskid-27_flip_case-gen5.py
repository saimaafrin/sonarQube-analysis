def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped_string = ''
    for letter in string:
        if letter.islower():
            flipped_string += letter.upper()
        else:
            flipped_string += letter.lower()
    return flipped_string
