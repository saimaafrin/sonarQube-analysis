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

    count_dot = 0
    count_digits = 0
    is_valid = False
    for i in file_name:
        if i == ".":
            count_dot += 1
        elif i.isdigit():
            count_digits += 1
    if count_dot == 1 and count_digits <= 3:
        for j in file_name.split(".")[0]:
            if j.isalpha():
                is_valid = True
        for k in file_name.split(".")[1]:
            if k in ["t", "x", "d"]:
                is_valid = is_valid and True
            else:
                is_valid = False
    if is_valid:
        return "Yes"
    else:
        return "No"
