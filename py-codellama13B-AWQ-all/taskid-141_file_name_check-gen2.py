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

    # check if there are more than three digits
    if file_name.count("0", "9") > 3:
        return "No"
    # check if there is one dot
    if file_name.count(".") != 1:
        return "No"
    # check if substring before dot is not empty and starts with a letter
    if not file_name[: file_name.index(".")].strip():
        return "No"
    if not file_name[: file_name.index(".")][0].isalpha():
        return "No"
    # check if substring after dot is one of these: ['txt', 'exe', 'dll']
    if file_name[file_name.index(".") + 1 :].strip() not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
