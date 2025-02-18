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

    file_name = file_name.replace(".", "").replace("\\", "")
    if len(file_name) > 3 or len(file_name) == 0 or file_name.startswith(" "):
        return "No"
    if not any(file_name[0].isalpha()) and not any(file_name[0].isdigit()):
        return "No"
    else:
        if any(file_name.endswith(x) for x in ("txt", "exe", "dll")):
            return "Yes"
        else:
            return "No"
