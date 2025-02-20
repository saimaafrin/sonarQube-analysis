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

    # check if the number of digits in file_name is less than 4
    if file_name.count(str(0)) >= 4:
        return 'No'
    # check if there is a dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    # check if the substring before the dot is not empty and starts with a letter
    if len(file_name[:file_name.index('.')]) == 0 or not file_name[:file_name.index('.')].isalpha():
        return 'No'
    # check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if file_name[file_name.index('.') + 1:] not in ['txt', 'exe', 'dll']:
        return 'No'
    # if everything is okay return Yes
    return 'Yes'
