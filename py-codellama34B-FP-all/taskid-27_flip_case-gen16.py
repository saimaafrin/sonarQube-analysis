def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flip = {}
    for i in range(97, 123):
        flip[chr(i)] = chr(i - 32)
    for i in range(65, 91):
        flip[chr(i)] = chr(i + 32)
    return ''.join(flip.get(char, char) for char in string)
