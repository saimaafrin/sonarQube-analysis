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

    # create a dictionary to check the file name
    valid_file_name = {
        '1': 'No',
        '2': 'No',
        '3': 'No',
        '4': 'No',
        '5': 'No',
        '6': 'No',
        '7': 'No',
        '8': 'No',
        '9': 'No',
        '0': 'No',
        'a': 'Yes',
        'b': 'Yes',
        'c': 'Yes',
        'd': 'Yes',
        'e': 'Yes',
        'f': 'Yes',
        'g': 'Yes',
        'h': 'Yes',
        'i': 'Yes',
        'j': 'Yes',
        'k': 'Yes',
        'l': 'Yes',
        'm': 'Yes',
        'n': 'Yes',
        'o': 'Yes',
        'p': 'Yes',
        'q': 'Yes',
        'r': 'Yes',
        's': 'Yes',
        't': 'Yes',
        'u': 'Yes',
        'v': 'Yes',
        'w': 'Yes',
        'x': 'Yes',
        'y': 'Yes',
        'z': 'Yes',
        'A': 'Yes',
        'B': 'Yes',
        'C': 'Yes',
        'D': 'Yes',
        'E': 'Yes',
        'F': 'Yes',
        'G': 'Yes',
        'H': 'Yes',
        'I': 'Yes',
        'J': 'Yes',
        'K': 'Yes',
        'L': 'Yes',
        'M': 'Yes',
        'N': 'Yes',
        'O': 'Yes',
        'P': 'Yes',
        'Q': 'Yes',
        'R': 'Yes',
        'S': 'Yes',
        'T': 'Yes',
        'U': 'Yes',
        'V': 'Yes',
        'W': 'Yes',
        'X': 'Yes',
        'Y': 'Yes',
        'Z': 'Yes',
        '.': 'Yes'
    }
    # create a list to check the file type
    valid_file_type = ['txt', 'exe', 'dll']

    # check if there are more than 3 numbers in the file name
    numbers = 0
    for i in file_name:
        if i.isdigit():
            numbers += 1
        if numbers > 3:
            return 'No'
    
    # check the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # check if the substring before the dot starts with a letter from the latin alphapet
    if valid_file_name[file_name[0]] == 'No':
        return 'No'
    
    # check if the substring after the dot is one of the following: 'txt', 'exe', 'dll'
    file_type = file_name[file_name.index('.') + 1:]
    if file_type not in valid_file_type:
        return 'No'

    return 'Yes'
