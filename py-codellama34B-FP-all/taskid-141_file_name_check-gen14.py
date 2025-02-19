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

    # Count how many digits we have in the string
    count = 0
    for c in file_name:
        if c.isdigit():
            count += 1
    if count > 3:
        return 'No'

    # Now we check if we have exactly one dot.
    dot_count = 0
    for i in range(len(file_name)):
        if file_name[i] == '.':
            dot_count += 1
    if dot_count != 1:
        return 'No'

    # Now we check if the substring before the dot is not empty and starts with a letter.
    dot_index = file_name.index('.')
    if dot_index == 0 or not file_name[0].isalpha():
        return 'No'

    # Now we check if the substring after the dot is txt, exe or dll
    if file_name[dot_index + 1:] not in ('txt', 'exe', 'dll'):
        return 'No'

    return 'Yes'
