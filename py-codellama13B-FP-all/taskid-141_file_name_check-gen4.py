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


    condition_1 = file_name.count('0') < 4 and file_name.count('1') < 4 and file_name.count('2') < 4 and file_name.count('3') < 4 and file_name.count('4') < 4 and file_name.count('5') < 4 and file_name.count('6') < 4 and file_name.count('7') < 4 and file_name.count('8') < 4 and file_name.count('9') < 4
    condition_2 = file_name.count('.') == 1
    condition_3 = len(file_name[0:file_name.index('.')]) > 0
    condition_4 = file_name[0:file_name.index('.')].isalpha()
    condition_5 = file_name[file_name.index('.')+1:] == 'txt' or file_name[file_name.index('.')+1:] == 'exe' or file_name[file_name.index('.')+1:] == 'dll'
    return 'Yes' if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 else 'No'
