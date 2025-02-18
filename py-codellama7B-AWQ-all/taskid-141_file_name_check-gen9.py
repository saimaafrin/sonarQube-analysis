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

    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif file_name[0] not in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']:
        return 'No'
    elif file_name.split('.')[-1] not in ['exe', 'dll', 'txt']:
        return 'No'
    else:
        return 'Yes'
