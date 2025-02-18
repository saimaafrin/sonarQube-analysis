def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # TODO: Implement me!

    def flip_case(string: str) -> str:
        new_string = ""
        for char in string:
            if char.islower():
                new_string += char.upper()
            else:
                new_string += char.lower()
        return new_string
    return flip_case(string)
