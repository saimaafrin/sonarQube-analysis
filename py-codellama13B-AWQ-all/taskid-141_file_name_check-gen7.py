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

    file_name_list = list(file_name)
    count = 0
    for i in file_name_list:
        if i.isdigit():
            count += 1
    if count > 3:
        return "No"
    if '.' not in file_name:
        return "No"
    if len(file_name.split('.')[0]) == 0:
        return "No"
    if file_name.split('.')[0][0].isalpha() == False:
        return "No"
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
