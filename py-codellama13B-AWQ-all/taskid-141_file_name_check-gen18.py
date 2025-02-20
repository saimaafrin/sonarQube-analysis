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

    file_name_lst = file_name.split(".")
    if len(file_name_lst) != 2:
        return 'No'
    else:
        before_dot = file_name_lst[0]
        after_dot = file_name_lst[1]
        if len(before_dot) == 0:
            return 'No'
        elif len(before_dot) > 3:
            return 'No'
        else:
            if after_dot not in ['txt', 'exe', 'dll']:
                return 'No'
            else:
                return 'Yes'
