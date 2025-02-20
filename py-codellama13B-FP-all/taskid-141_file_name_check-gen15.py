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

    # Here we check if the input is of the correct type
    if not isinstance(file_name, str):
        raise ValueError("Input must be a string")

    # Here we check if the file name is valid
    if not len(file_name.split('.')) == 2:
        return "No"

    substring_before_dot = file_name.split('.')[0]
    substring_after_dot = file_name.split('.')[1]

    # Here we check if the substring before the dot is valid
    if len(substring_before_dot) == 0 or not (substring_before_dot[0].isalpha() or substring_before_dot[0].isupper()):
        return "No"

    # Here we check if the substring after the dot is valid
    if not substring_after_dot in ['txt', 'exe', 'dll']:
        return "No"

    # Here we check if the file name contains more than three digits
    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return "No"

    return "Yes"
