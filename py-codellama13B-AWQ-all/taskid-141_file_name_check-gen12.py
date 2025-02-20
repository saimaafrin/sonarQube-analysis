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
    dot_index = 0
    for i in range(len(file_name)):
        if file_name[i] == '.':
            dot_index = i
            break
        if '0' <= file_name[i] <= '9':
            count += 1
    if count > 3 or dot_index == 0:
        return 'No'

    substring = file_name[:dot_index]
    if not substring:
        return 'No'
    if not 'a' <= substring[0] <= 'z' and not 'A' <= substring[0] <= 'Z':
        return 'No'

    substring = file_name[dot_index+1:]
    if substring == 'txt' or substring == 'exe' or substring == 'dll':
        return 'Yes'
    return 'No'
