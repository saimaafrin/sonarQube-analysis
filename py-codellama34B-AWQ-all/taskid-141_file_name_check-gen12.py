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

    file_name_list = file_name.split('.')

    if file_name_list[0].isalpha() == False:
        return 'No'

    if len(file_name_list) != 2:
        return 'No'

    if len(file_name_list[0]) == 0:
        return 'No'

    if file_name_list[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    digit_count = 0
    for char in file_name_list[0]:
        if char.isdigit():
            digit_count += 1
            if digit_count > 3:
                return 'No'

    return 'Yes'
