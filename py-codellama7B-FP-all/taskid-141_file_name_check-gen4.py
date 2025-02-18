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


    digits = len([char for char in file_name if char.isdigit()])
    dot_index = file_name.index('.') if '.' in file_name else -1
    return 'Yes' if (
        digits <= 3 and
        dot_index > 0 and
        file_name[0] in string.ascii_letters and
        file_name[dot_index+1:].lower() in ['txt', 'exe', 'dll']
    ) else 'No'
