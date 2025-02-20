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

    count = 0
    dot_count = 0
    for i in file_name:
        if i.isdigit():
            count += 1
            if count > 3:
                return 'No'
        if i == '.':
            dot_count += 1
            if dot_count > 1:
                return 'No'
    if count > 3:
        return 'No'
    if dot_count != 1:
        return 'No'
    else:
        if file_name[0].isalpha():
            if file_name[len(file_name)-4:len(file_name)] in ('txt', 'exe', 'dll'):
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
