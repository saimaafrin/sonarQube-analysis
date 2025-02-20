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

    if len(file_name) < 3:
        return "No"

    count_dot = 0
    count_digit = 0
    count_letter = 0
    count_letters_before_dot = 0

    for i in range(len(file_name)):
        if file_name[i].isdigit():
            count_digit += 1
        elif file_name[i] == ".":
            count_dot += 1
        elif file_name[i].isalpha():
            count_letter += 1
            if count_dot != 1:
                count_letters_before_dot += 1

    if (
        count_dot == 1
        and count_digit <= 3
        and count_letter == len(file_name)
        and count_letters_before_dot != 0
    ):
        return "Yes"
    else:
        return "No"
