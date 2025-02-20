def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # Convert string to list
    str_list = list(string)

    # For each character in list, flip case
    for i in range(len(str_list)):
        if str_list[i].islower():
            str_list[i] = str_list[i].upper()
        elif str_list[i].isupper():
            str_list[i] = str_list[i].lower()

    return ''.join(str_list)
