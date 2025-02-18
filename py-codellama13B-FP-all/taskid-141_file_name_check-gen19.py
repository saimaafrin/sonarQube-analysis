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


    # checking if the file has more than three digits
    digits = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
        if digits > 3:
            return 'No'

    # checking if the file has a dot
    has_dot = False
    for char in file_name:
        if char == '.':
            has_dot = True
            break
    if not has_dot:
        return 'No'

    # checking if the substring before the dot starts with a letter and is not empty
    before_dot = ''
    for char in file_name:
        if char == '.':
            break
        before_dot += char
    if not before_dot:
        return 'No'
    if not before_dot[0].isalpha():
        return 'No'

    # checking if the substring after the dot is one of ['txt', 'exe', 'dll']
    after_dot = ''
    for char in file_name:
        if char == '.':
            continue
        after_dot += char
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
