def file_name_check(file_name: str) -> str:
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    >>> file_name_check('example.txt')
    'Yes'
    >>> file_name_check('1example.dll')
    'No'
    """

    if file_name.count(".") != 1:
        return "No"
    first_dot = file_name.find(".")
    if first_dot == 0:
        return "No"
    elif first_dot == (len(file_name) - 1):
        return "No"
    else:
        first_part = file_name[:first_dot]
        second_part = file_name[first_dot + 1 :]
        if len(first_part) > 3:
            return "No"
        elif first_part[0].isalpha() is False:
            return "No"
        elif second_part == "txt" or second_part == "exe" or second_part == "dll":
            return "Yes"
        else:
            return "No"
