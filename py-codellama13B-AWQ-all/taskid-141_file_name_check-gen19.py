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

    if len(file_name) > 12 or file_name.count('.') != 1 or file_name.count(
        '..') > 0 or file_name[0].isdigit() or file_name[-1].isdigit() or file_name[0] == '.':
        return "No"

    before_dot, after_dot = file_name.split('.')
    if len(before_dot) == 0 or not (before_dot[0].isalpha()):
        return "No"

    if after_dot not in ["txt", "exe", "dll"]:
        return "No"

    return "Yes"
