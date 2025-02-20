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

    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') > 3:
        return 'No'
    if file_name.count('a') + file_name.count('b') + file_name.count('c') + file_name.count('d') + file_name.count('e') + file_name.count('f') + file_name.count('g') + file_name.count('h') + file_name.count('i') + file_name.count('j') + file_name.count('k') + file_name.count('l') + file_name.count('m') + file_name.count('n') + file_name.count('o') + file_name.count('p') + file_name.count('q') + file_name.count('r') + file_name.count('s') + file_name.count('t') + file_name.count('u') + file_name.count('v') + file_name.count('w') + file_name.count('x') + file_name.count('y') + file_name.count('z') + file_name.count('A') + file_name.count('B') + file_name.count('C') + file_name.count('D') + file_name.count('E') + file_name.count('F') + file_name.count('G') + file_name.count('H') + file_name.count('I') + file_name.count('J') + file_name.count('K') + file_name.count('L') + file_name.count('M') + file_name.count('N') + file_name.count('O') + file_name.count('P') + file_name.count('Q') + file_name.count('R') + file_name.count('S') + file_name.count('T') + file_name.count('U') + file_name.count('V') + file_name.count('W') + file_name.count('X') + file_name.count('Y') + file_name.count('Z') > 0:
        return 'No'
    if file_name.index('.') == 0:
        return 'No'
    if file_name.index('.') == (len(file_name) - 1):
        return 'No'
    if file_name.find('.') == -1:
        return 'No'
    if file_name.split('.')[0] == '':
        return 'No'
    if file_name.split('.')[0][0] < 'a' or file_name.split('.')[0][0] > 'z' or file_name.split('.')[0][0] < 'A' or file_name.split('.')[0][0] > 'Z':
        return 'No'
    if file_name.split('.')[1] != 'txt' and file_name.split('.')[1] != 'exe' and file_name.split('.')[1] != 'dll':
        return 'No'
    return 'Yes'
