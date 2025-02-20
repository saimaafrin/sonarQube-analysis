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

    # 1. Check for '.'
    if '.' not in file_name:
        return 'No'
    # 2. Check for letters before '.'
    if file_name[:file_name.index('.')] == '':
        return 'No'
    # 3. Check for letters after '.'
    if not file_name[file_name.index('.') + 1:] in ['txt', 'exe', 'dll']:
        return 'No'
    # 4. Check for digits
    if len(re.findall('[0-9]', file_name)) > 3:
        return 'No'
    return 'Yes'
