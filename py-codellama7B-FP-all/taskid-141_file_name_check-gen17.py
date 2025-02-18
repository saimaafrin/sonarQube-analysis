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

    if file_name.count('.') > 1:
        return 'No'
    elif file_name.count('.') == 0:
        return 'No'
    elif file_name.count('.') == 1:
        if file_name.endswith('.txt') or file_name.endswith('.exe') or file_name.endswith('.dll'):
            if file_name.count('0') > 2:
                return 'No'
            elif file_name.count('0') == 2:
                if file_name.startswith(file_name[0] + file_name[1] + file_name[2]):
                    return 'Yes'
                else:
                    return 'No'
            else:
                return 'Yes'
        else:
            return 'No'
