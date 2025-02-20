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

    # Check if there are more than 3 digits
    if len(re.findall(r'\d+', file_name)) > 3:
        return 'No'
    # Check if there is one and only one dot
    if len(re.findall(r'\.', file_name)) != 1:
        return 'No'
    # Check if the substring before the dot is not empty and starts with a letter
    substring_before_dot = re.search(r'^[^.]+', file_name).group(0)
    if len(substring_before_dot) == 0 or not substring_before_dot.isalpha():
        return 'No'
    # Check if the substring after the dot is one of the following: ['txt', 'exe', 'dll']
    substring_after_dot = re.search(r'\.[^.]+', file_name).group(0)[1:]
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    # If the code reaches this point, it means the file name is valid
    return 'Yes'
