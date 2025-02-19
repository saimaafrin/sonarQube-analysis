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

    number_of_digits = 0
    is_dot_appeared = False
    for ch in file_name:
        if ch.isdigit():
            number_of_digits += 1
        if ch == ".":
            is_dot_appeared = True
            break
    if not is_dot_appeared:
        return "No"
    if number_of_digits > 3:
        return "No"
    last_dot_index = file_name.rfind(".")
    if last_dot_index == 0 or file_name[last_dot_index - 1] == ".":
        return "No"
    if file_name[last_dot_index + 1:] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
