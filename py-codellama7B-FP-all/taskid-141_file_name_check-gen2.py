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

    number_count = 0
    for char in file_name:
        if char.isdigit():
            number_count += 1
    if number_count > 3:
        return 'No'
    if '.' in file_name:
        dot_index = file_name.index('.')
        if dot_index == 0:
            return 'No'
        if file_name[0].isalpha():
            if file_name[dot_index + 1] in ['txt', 'exe', 'dll']:
                return 'Yes'
            return 'No'
        return 'No'
    return 'No'
