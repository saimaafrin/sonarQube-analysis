def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return "".join([chr(97 + ord(c) - ord("a")) if ord(c) > 96 else chr(65 + ord(c) - ord("A")) for c in string])
